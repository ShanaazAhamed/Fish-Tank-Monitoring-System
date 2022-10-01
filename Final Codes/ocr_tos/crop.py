# Importing Image class from PIL module
from PIL import Image


def crop_img(left=200,top=2.3,right=580,bottom=4):
    im = Image.open("/home/pi/Final Codes/ocr_tos/img/a.jpg")
    width, height = im.size
    top = height / top
    bottom = 3 * height / bottom
    im1 = im.crop((left, top, right, bottom))
    im1.save("/home/pi/Final Codes/ocr_tos/img/a1.jpg")
    #im1.show()
    
    
if __name__ == '__main__':
    crop_img()
    print("crop done")