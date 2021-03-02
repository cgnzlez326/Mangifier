from PIL import Image
from PIL import ImageFile


def img_loader(f_image, s_image=None):
    ImageFile.LOAD_TRUNCATED_IMAGES = True
    img = Image.new('RGB', (1696, 1212), color=-1)

    if s_image is not None:
        img1 = Image.open(f_image)
        img2 = Image.open(s_image)
    else:
        img1 = Image.open(f_image)
        img2 = Image.new('RGB', (838, 1189), color=-1)

    img1 = img1.resize((838, 1185))
    img2 = img2.resize((838, 1185))
    img.paste(img1, (5, 16))
    img.paste(img2, (853, 16))
    return img
