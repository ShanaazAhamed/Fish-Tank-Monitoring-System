from picamera import PiCamera
#import picamera
from time import sleep


def capture(): 
    camera = PiCamera()
    camera.start_preview()
    sleep(5)
    camera.capture('/home/pi/Final Codes/ocr_tos/img/a.jpg')
    camera.stop_preview()
    camera.close()
    
if __name__ == '__main__':
    capture()
    print("capture done")

