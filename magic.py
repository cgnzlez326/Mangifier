from pdf import merge
from imports import import_images

img_1 = []
img_2 = []
path = None

if __name__ == '__main__':
    img_1, img_2, path = import_images.load_images()
    merge.merge(img_1, img_2, path)
