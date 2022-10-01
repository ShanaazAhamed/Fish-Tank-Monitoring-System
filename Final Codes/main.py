from firebase_db.push_db import fetch_to_firebase,get_tokens,feed_now
import feeder.feeder as feeder
from ph_arduino.ph import get_ph_value
import serial
from datetime import datetime,date
import firebase_cloud_msg.FCMMessage as fcm
import ocr_tos.ocr_tos as ocr
import ocr_tos.camera_snap as camera
import ocr_tos.crop as crop


#sensor_data ={"Turbidity":"Normal","PH Value":6.8,"PH Status":"Good","Available food":5,"Need Feeding":"Yes"}
sensor_data = {}


if __name__ == '__main__':
    try:
        while True:
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            today = date.today()
            last_update = "{}/{}/{}".format(str(today.year),str(today.month),str(today.day)) + "  " + now.strftime("%H:%M") 
            
            try:
                feed_now_btn = feed_now("Sensor Data")
                if feed_now_btn == "True":
                    feeder.start_servo()
                    dist = feeder.cal_distance()
                    print(dist)
                    sensor_data["Available food"]= round(((10.8-dist)/10.8)*100)
                    feed_now_btn = "False"
                    sensor_data["Feed Now"] = feed_now_btn
                    sensor_data["LastFeeder"] = last_update
                    fetch_to_firebase("Sensor Data",sensor_data)
                    
                    
            except:
                print("No internet Connection")
            
            if current_time in ["06:00:00","16:00:00","00:14:00","17:22:00","17:42:00","15:43:00"]:
                dist = feeder.cal_distance()
                sensor_data["Available food"]= round(((10.8-dist)/10.8)*100)
                if sensor_data["Available food"] < 20:
                    sensor_data["Need Feeding"] = "Yes"
                    try:
                        tokens = get_tokens("Tokens")
                        fcm.sendPush("Feeder","Please fill feeding bottle", tokens)
                    except:
                        print("Please connect to the internet0")
                        
                else:
                    sensor_data["Need Feeding"] = "No"
                 
                feed = feeder.check_distance(dist)
                if feed:
                    feeder.start_servo()
                    dist = feeder.cal_distance()
                    sensor_data["Available food"]= round(((10.8-dist)/10.8)*100)
                try:
                    tokens = get_tokens("Tokens")
                    sensor_data["LastFeeder"] = last_update
                    fetch_to_firebase("Sensor Data",sensor_data)
                except:
                    print("Please connect to the internet1")
                    
            
            if current_time in ["08:00:00","14:00:00","20:00:00","00:14:00","17:21:00","15:40:00"]: 
                sensor_data["PH Value"] = get_ph_value()
                #print(sensor_data["PH Value"])
                if sensor_data["PH Value"] >= 6 and sensor_data["PH Value"] <=8:
                    sensor_data["PH Status"] = "Good"
                elif sensor_data["PH Value"] >= 8:
                    sensor_data["PH Status"] = "High PH"
                    try:
                        tokens = get_tokens("Tokens")
                        fcm.sendPush("PH","Please descrease the PH Value", tokens)
                    except:
                        print("Please connect to the internet2")
                else:
                    sensor_data["PH Status"] = "Low PH"
                    try:
                        tokens = get_tokens("Tokens")
                        fcm.sendPush("PH","Please increase the PH Value", tokens)
                    except:
                        print("Please connect to the internet2")
                try:
                    camera.capture()
                    crop.crop_img()
                    sensor_data["Turbidity"]=ocr.ocr()
                except:
                    print("Please connect to the internet2")
                
                if sensor_data["Turbidity"] != "good":
                    i = 0
                    while(i<3):
                        camera.capture()
                        crop.crop_img()
                        sensor_data["Turbidity"]=ocr.ocr()
                        i+=1
                if  sensor_data["Turbidity"] != "good":
                    try:
                        tokens = get_tokens("Tokens")
                        fcm.sendPush("Turbidity",sensor_data["Turbidity"], tokens)
                    except ConnectionError:
                        print("Please connect to the internet3")
                        
                
                try:
                    sensor_data["LastPh"] = last_update
                    fetch_to_firebase("Sensor Data",sensor_data)
                except ConnectionError:
                    print("Please connect to the internet4")
                    
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
        
        
         