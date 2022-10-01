from pickletools import uint8
import cv2
import pytesseract
import numpy as np


def ocr_core(img):
    text = pytesseract.image_to_string(img)
    return text

def get_grayscale(img):
    return cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)

def remove_noise(img):
    kernel = np.ones((1,1),np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    kernel = np.ones((1,1),np.uint8)
    img = cv2.erode(img,kernel, iterations=1)
    img = cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel)
    img = cv2.medianBlur(img,3)
    return (img)


def thresholding(img,level):
    return cv2.threshold(img,level,255,cv2.THRESH_BINARY)[1]

#level_select_noise = {1:170,2:126,3:116,}
#level_select_no_noise = {1:172,2:137,3:119}
#level = int(input("please enter the level for warning 0 means warn on less turbid and 3 means warn on more turbid : "))

def ocr():
    img = cv2.imread('/home/pi/Final Codes/ocr_tos/img/a1.jpg')
    img = get_grayscale(img)
#img = thresholding(img,level_select_no_noise[level]) #0 means black and the 255 means white
    img = thresholding(img,82)
    img = remove_noise(img)
    txt = ocr_core(img)
    #print(txt)
    txt = txt.split(" ")
    print(txt)
    #cv2.imshow('Result', img)
    
    if "Helllo" in txt[0]:
        return ("good")
    
    elif ("Hellio" in txt[0]) or ("Helilo" in txt[0]):
        return ("not bad at all")
    #recheck

    else:
        return ("Need change")
    
    #rechek
    #print(ocr_core(img))
    
    cv2.waitKey(0)

if __name__ == '__main__':
    #Capture()
    #crop_img()
    ocr()
    