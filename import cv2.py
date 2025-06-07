import cv2
from PIL import Image
import numpy as np
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
'''
def read_image_PIL(path):
    im = Image.open(path)
    try:
        print(im)
    except:
        print(type(im))
    im.show()
    return im'''
image = read_image_cv('pl.webp')
#image_pilllow = read_image_PIL('pl.webp')

def reverse_img(img):
    new_img = []
    for row in range(img.shape[0]):
        new_row = []
        for column in range(img.shape[1]):
            new_row.append(img[-1-row][column])
        new_img.append(new_row)
    return np.array(new_img)
show_image(reverse_img(image))
        
def reverse_img_short(img):
    img_reverse=img[::-1]
    return img_reverse
show_image(reverse_img_short(image))

show_image(cv2.flip(image,0))