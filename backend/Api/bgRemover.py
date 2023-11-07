import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import cv2
import uuid
import os
import base64
from PIL import Image
from model import U2NET
from torch.autograd import Variable
from skimage import io, transform, img_as_ubyte
import io as sysio

# import skimage
from PIL import Image

# Get The Current Directory
currentDir = os.path.dirname(__file__)

# Functions:

# ------- Load Trained Model --------
print("---Loading Model---")
model_name = 'u2net'
model_dir = os.path.join(currentDir, 'saved_models',
                         model_name, model_name + '.pth')
net = U2NET(3, 1)
if torch.cuda.is_available():
    net.load_state_dict(torch.load(model_dir))
    net.cuda()
else:
    net.load_state_dict(torch.load(model_dir, map_location='cpu'))


def save_output(image_np, predict):
    predict = predict.squeeze()
    predict_np = predict.cpu().data.numpy()
    im = Image.fromarray(predict_np * 255).convert('RGB')
    imo = im.resize((image_np.shape[1], image_np.shape[0]))
    pb_np = np.array(imo)

    # Make and apply mask
    mask = pb_np[:, :, 0]
    mask = np.expand_dims(mask, axis=2)
    imo = np.concatenate((image_np, mask), axis=2)
    imo = Image.fromarray(imo, 'RGBA')

    image_as_ubyte = img_as_ubyte(imo)
    pil_image = Image.fromarray(image_as_ubyte)

    pil_image = crop_transparent(pil_image)
    pil_image = resizeImg(pil_image)

    # pil image -> binar ->base65(string)
    buffer = sysio.BytesIO()
    pil_image.save(buffer, format="PNG")
    image_binary = buffer.getvalue()
    base64_string = base64.b64encode(image_binary).decode("utf-8")

    # photo_data = base64.b64decode(base64_string)
    # with open("compare.jpg", "wb") as file:
    #     file.write(photo_data)
    return base64_string


def resizeImg(image):
    new_width = 300
    new_height = 300
    resized_image = image.resize((new_width, new_height))
    return resized_image


def crop_transparent(image):
    # Obține matricea de pixeli și canalul de transparență (alfa)
    image_data = np.asarray(image)
    alpha_channel = image_data[:, :, 3]

    # Găsește limitele zonei opace și parțial transparente
    non_transparent_rows = np.any(alpha_channel > 100, axis=1)
    non_transparent_columns = np.any(alpha_channel > 100, axis=0)
    top, bottom = np.where(non_transparent_rows)[0][[0, -1]]
    left, right = np.where(non_transparent_columns)[0][[0, -1]]

    # Taie imaginea în funcție de limitele găsite
    cropped_image_data = image_data[top:bottom + 1, left:right + 1, :]

    # Creează o nouă imagine pe baza matricei de pixeli croită
    cropped_image = Image.fromarray(cropped_image_data)

    (width, height) = cropped_image.size
    border_w = 0
    border_h = 0
    if width > height:
        border_h = (width - height) // 2
        height += border_h * 2
    else:
        border_w = (height - width) // 2
        width += border_w * 2

    # Create a new image object for the output image
    box_image = Image.new("RGBA", (width, height), (0, 0, 0, 0))

    # Paste the cropped image onto the new image
    box_image.paste(cropped_image, (border_w, border_h))

    return box_image


def fix_image_orientation(image_binary):
    try:
        # Convertim imaginea binară în obiectul Image folosind Pillow
        img = Image.open(sysio.BytesIO(image_binary))

        # Verificăm dacă imaginea conține metadate de orientare
        if hasattr(img, '_getexif') and img._getexif() is not None:
            exif = dict(img._getexif().items())
            orientation = exif.get(0x0112)

            # Rotim imaginea în funcție de orientare (dacă este necesar)
            if orientation == 3:
                img = img.rotate(180, expand=True)
            elif orientation == 6:
                img = img.rotate(270, expand=True)
            elif orientation == 8:
                img = img.rotate(90, expand=True)

        # Convertim imaginea înapoi în șir de octeți (bytes) pentru a o returna
        buffer = sysio.BytesIO()
        img.save(buffer, format='PNG')
        buffer.seek(0)

        return buffer.getvalue()

    except Exception as e:
        print("Eroare:", str(e))
        return None


def removeBg(img_binary):
    # inputs_dir = os.path.join(currentDir, 'cache')

    # convert string of image data to uint8

    img_binary = fix_image_orientation(img_binary)
    img = bytearray(img_binary)

    nparr = np.frombuffer(img, np.uint8)

    if len(nparr) == 0:
        return '---Empty image---'

    # decode image
    try:
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    except:
        return "---Empty image---"

    # save base img
    image_stream = sysio.BytesIO(img_binary)
    image = Image.open(image_stream)
    image_np = np.asarray(image)

    # processing
    image = transform.resize(img, (320, 320), mode='constant')

    tmpImg = np.zeros((image.shape[0], image.shape[1], 3))

    tmpImg[:, :, 0] = (image[:, :, 0] - 0.485) / 0.229
    tmpImg[:, :, 1] = (image[:, :, 1] - 0.456) / 0.224
    tmpImg[:, :, 2] = (image[:, :, 2] - 0.406) / 0.225

    tmpImg = tmpImg.transpose((2, 0, 1))
    tmpImg = np.expand_dims(tmpImg, 0)
    image = torch.from_numpy(tmpImg)

    image = image.type(torch.FloatTensor)
    image = Variable(image)

    d1, d2, d3, d4, d5, d6, d7 = net(image)
    pred = d1[:, 0, :, :]
    ma = torch.max(pred)
    mi = torch.min(pred)
    dn = (pred - mi) / (ma - mi)
    pred = dn

    return save_output(image_np, pred)
