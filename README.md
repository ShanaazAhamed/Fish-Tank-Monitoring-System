# Fish Tank Monitoring System

<img src="https://user-images.githubusercontent.com/77115237/190552397-5318eeb5-e281-4473-b809-dc97bcf0f1cd.png" width="100%" height = "auto">
<!--![image](https://user-images.githubusercontent.com/77115237/190552397-5318eeb5-e281-4473-b809-dc97bcf0f1cd.png)-->
Fish and other aquatic animals need a balanced pH for survival of them. This pH value can make fish sick and  even kill them. Therefore, we are proposing a system for fish tanks which monitors the value of pH using the pH  sensor and alert the specific person using notification. There after we can add baking soda to raise the pH and add peat moss to lower the pH value. We also do check the turbidity of water using the camera and image  processing. In addition to that we propose an automated feeding system at regular intervals.

## Project Scope 
<p>This project will focus on developing a pH meter using an analog pH meter, conversion module and Arduino for pH monitoring. For turbidity monitoring, we use camera module and cover software parts.
This project will include, </p>

- PH monitoring system using Analog pH sensor, BNC connector which is connected to the raspberry pi 3 B+ and display the real time output to the LCD showing current pH value and the range of the suitable pH value. When the pH value changes out of the range the display will output a message saying that 
the pH out of range on the android app.

- Turbidity checking system which uses a omni vision 5647 5MP camera module, image processing to check the turbidity and notify when to change the water by push notification
- Automatic feeding system which feed the fish at regular intervals using the servo motor, small container, ultrasonic sensor. The ultrasonic sensor is used to check the amount feed that is available and use the same notification system to communicate with the owner when the feed is low. Servo motor will operate at regular intervals using the time of raspberry pi which is connected to the internet as raspberry pi 3 B+ already have an in-built WIFI.


## Operating Environment 
<p align="center">
<img src="https://user-images.githubusercontent.com/77115237/190553010-fe8954f2-1ebe-496d-b03d-0f732ae6d988.png" width="50%" height = "auto">
</p>

### Our system mainly contains three main parts
  1. PH monitoring system
  2. Turbidity monitoring
  3. Automated Feeding system

### All are monitored and displayed through the android app

We have built an android app to monitor pH value, whether turbid or not, feed level. In addition to that we have added feed now button to feed the system manually instantly from anywhere. We use firebase to store data. 

<p align="center">
<img src="https://user-images.githubusercontent.com/77114773/197248711-8e8e52cc-1827-4a81-9425-cf471a50d302.jpeg" width="auto" height = "500px">
</p>

### pH monitoring system

We use the `pH probe` with `BNC electrode` to measure the pH value. We use `arduino UNO` to get the readings as the pH module produces analog output. We cannot connect the pH sensor kit with the `raspberry Pi`. Our whole system is intergrated with Raspberry Pi and this is the only component that cannot be connected with the RPi. So we read using the Arduino UNO board and then send the values to the raspberry Pi using `serial communication`. Before starting the rreadings we need to calibrate the pH sensor with the provided pH solutions in order to aquire a higher accuray.

### code for measuring the pH value

~~~
#include <Wire.h>
//#include <Adafruit_GFX.h>
//#include <Adafruit_SSD1306.h>
//#include <SimpleTimer.h>
 
//SimpleTimer timer;
 
float calibration_value = 21.34+0.42 ;
int phval = 0; 
unsigned long int avgval; 
int buffer_arr[10],temp;
 
float ph_act;
// for the OLED display
 
//#define SCREEN_WIDTH 128 // OLED display width, in pixels
//#define SCREEN_HEIGHT 64 // OLED display height, in pixels
// 
//// Declaration for an SSD1306 display connected to I2C (SDA, SCL pins)
//#define OLED_RESET     -1 // Reset pin # (or -1 if sharing Arduino reset pin)
//Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);
// 
void setup() 
{
  Wire.begin();
 Serial.begin(9600);
//  display.begin(SSD1306_SWITCHCAPVCC, 0x3C);
//  display.clearDisplay();
//  display.setTextColor(WHITE); 
 
 
//timer.setInterval(500L, display_pHValue);
}
void loop() {
//  timer.run(); // Initiates SimpleTimer
 for(int i=0;i<10;i++) 
 { 
 buffer_arr[i]=analogRead(A0);
 delay(30);
 }
 for(int i=0;i<9;i++)
 {
 for(int j=i+1;j<10;j++)
 {
 if(buffer_arr[i]>buffer_arr[j])
 {
 temp=buffer_arr[i];
 buffer_arr[i]=buffer_arr[j];
 buffer_arr[j]=temp;
 }
 }
 }
 avgval=0;
 for(int i=2;i<8;i++)
 avgval+=buffer_arr[i];
 float volt=(float)avgval*5.0/1024/6; 
  ph_act = -5.70 * volt + calibration_value;
 
 Serial.print(ph_act);
 delay(1000);
}
~~~ 
 
### Code for voltage calibration of the pH sensor

```
int pH_Value; 
float Voltage;
 
void setup() 
{ 
  Serial.begin(9600);
  pinMode(pH_Value, INPUT); 
} 
 
void loop() 
{ 
  pH_Value = analogRead(A0); 
  Voltage = pH_Value * (5.0 / 1023.0); 
  Serial.println(Voltage); 
  delay(500); 
}

```
<img src="https://user-images.githubusercontent.com/77114773/197242007-fd786fd0-8f41-49d1-b598-8a99a87581db.jpeg" width="50%" height = "auto">
<img src="https://user-images.githubusercontent.com/77114773/197243025-b4cc25af-4432-4134-99ca-25ec3c9fb36e.png" width="50%" height = "auto">
source:www.electroniclinic.com



python code to recieve in the RPi is atached in the above final codes folder

<h3>Turbidity monitoring system</h3>
This is an OCR based approach to determine two states turbid or not turbid. We place a word inside the water and take the photo of the word and try to detect text using OCR. if the water is turbid the word would not be detected. For this we used openCV library for image processing and Tesseract OCR engine to perform OCR.
First we need to adjust a threshold value in the thresh function of the code to set our preferred turbidty as the threshold turbidity level beyond this would be turbid means text becomes undetected as we set threshold value.
Pi camera module is used to capture the image of the word. Then image processing gryescaling,noise reduction and then thresholding. Finally OCR for the particular processed image. The powerpoint presentation inside the Doucments directory explains how image processing is done. I have attached necessary python codes to the finalcodes/ocr_tos

![WhatsApp Image 2022-06-17 at 11 43 58 AM](https://user-images.githubusercontent.com/77114773/197246389-c1b8712e-22a5-42e4-a2ad-a81e00823fdb.jpeg)
![WhatsApp Image 2022-06-17 at 11 41 47 AM](https://user-images.githubusercontent.com/77114773/197246632-ed3052c6-555d-4dee-909d-6931f00408e3.jpeg)

<h3>Automated feeding system</h3>
We use servo motor attached with the bottle containing feed to operate by opening and closing the hole(feed dispenser) of the bottle. The servomotor is set to automatically operate by preset times daily (for eg : 8.00 am daily). There fore we donot need to feed manually.We can also use the feed now button in the android app to feed instantly from anywhere in the world. We use ultrasonic sensor to read the distance inside the bottle to calculate the amount of feed available inside the bottle. This amount will be updated as a percentage on the android dashboard. amount_feed = ((maximum_distance-present_distance)/maximum_distance)x100.

all the necessary codes are added in the finalcodes/feeder
![WhatsApp Image 2022-06-17 at 11 41 29 AM](https://user-images.githubusercontent.com/77114773/197248289-94b3f96e-c07c-4de4-b166-14f13834eb8d.jpeg)

whole system
![WhatsApp Image 2022-06-17 at 11 43 58 AM](https://user-images.githubusercontent.com/77114773/197248783-6f580b98-0f69-403b-a557-fd04d4f6ae0a.jpeg)


