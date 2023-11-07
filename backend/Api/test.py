import requests
import json
import base64
from PIL import Image

base = 'http://127.0.0.1:5000/'

# with open("1.jpg", "rb") as img:
#     img_string = base64.b64encode(img.read()).decode('utf-8')
#
# headers = {'accept': 'application/json'}

detalii = {
    "nume": "test1",
    "tip": "casual",
    "headId": 2253947988,
    "upperId": 2062143657,

}

response = requests.post(base + "outfit", json=detalii)

# photo_data = base64.b64decode(response.json()["imagine"])
# with open("compare.jpg", "wb") as file:
#     file.write(photo_data)

print(response)

# from PIL import Image
#
# images = []
# images.append(Image.open('m1.png'))
# images.append(Image.open('m2.png'))
# images_size = [img.size for img in images]
#
# new_image = Image.new('RGBA', (images_size[0][0], sum(images_size[1])), (250, 250, 250, 0))
#
# height = 0
# for img in images:
#     new_image.paste(img, (0, height))
#     height += img.size[1]
#
# new_image.save("merged.png", "PNG")
