from PIL import Image

def mergeImg(images):
    # images = []
    # images.append(Image.open('m1.png'))
    # images.append(Image.open('m2.png'))
    # print(images)
    images_size = [img.size for img in images]
    # print(images_size)

    height = 0
    for img in images:
        height += img.size[1]
    new_image = Image.new('RGBA', (images_size[0][0], height), (250, 250, 250, 0))

    height = 0
    for img in images:
        new_image.paste(img, (0, height))
        height += img.size[1]

    # new_image.save("merged.png", "PNG")
    return new_image