import cv2
from PIL import Image

def show_image(img):
    cv2.imshow('image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def read_image_cv(path):
    img = cv2.imread(path,cv2.IMREAD_COLOR)
    print(img)
    print(img.shape)
    print(type(img))
    show_image(img)
    return img

def read_image_PIL(path):
    im = Image.open(path)
    try:
        print(im)
    except:
        print(type(im))
    im.show()
    return im
image = read_image_cv('pl.webp')
image_pilllow = read_image_PIL('pl.webp')
