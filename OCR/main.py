from pickletools import uint8
import cv2
import pytesseract
import numpy as np

#pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"


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

# level_select_noise = {1:170,2:126,3:116,}
level_select_no_noise = {1:172,2:137,3:119}
level = int(input("please enter the level for warning 0 means warn on less turbid and 3 means warn on more turbid : "))

img = cv2.imread('2.jpeg')
img = get_grayscale(img)
img = thresholding(img,level_select_no_noise[level]) #0 means white and the 255 means black
img = remove_noise(img)
txt = ocr_core(img)
txt = txt.split(" ")
if "Helllo" not in txt:
    print("Needed to change the water")
#print(ocr_core(img))
#cv2.imshow('Result', img)
cv2.waitKey(0)
