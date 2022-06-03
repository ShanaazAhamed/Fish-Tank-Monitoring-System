import RPi.GPIO as GPIO
import time
from datetime import datetime

GPIO_TRIGGER = 18
GPIO_ECHO = 24

pwm_gpio = 17
frequence = 50


def angle_to_percent (angle) :
    if angle > 180 or angle < 0 :
        return False

    start = 4
    end = 12.5
    ratio = (end - start)/180 #Calcul ratio from angle to percent

    angle_as_percent = angle * ratio

    return start + angle_as_percent

def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance

def start_servo():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(pwm_gpio, GPIO.OUT)
    pwm = GPIO.PWM(pwm_gpio, frequence)
    pwm.start(angle_to_percent(0))
    time.sleep(1)
    pwm.ChangeDutyCycle(angle_to_percent(90))
    time.sleep(1)
    pwm.start(angle_to_percent(0))
    time.sleep(1)
    pwm.stop()
    GPIO.cleanup()
    
def cal_distance():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
    GPIO.setup(GPIO_ECHO, GPIO.IN)
    dist = distance()
    GPIO.cleanup()
    return dist

def check_distance(d):
    if round(float(d),1)>= 10:
        print("Needed to fill")
        return False
    else:
        return True

if __name__ == '__main__':
    try:
        while True:
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            
            if current_time in ["08:00:00","16:00:00","11:56:20"]:
                dist = cal_distance()
                feed = check_distance(dist)
                if feed:
                    start_servo()
                
               
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
    