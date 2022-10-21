# Fish Tank Monitoring System

<img src="https://user-images.githubusercontent.com/77115237/190552397-5318eeb5-e281-4473-b809-dc97bcf0f1cd.png" width="100%" height = "auto">
<!--![image](https://user-images.githubusercontent.com/77115237/190552397-5318eeb5-e281-4473-b809-dc97bcf0f1cd.png)-->
Fish and other aquatic animals need a balanced pH for survival of them. This pH value can make fish sick and  even kill them. Therefore, we are proposing a system for fish tanks which monitors the value of pH using the pH  sensor and alert the specific person using notification. There after we can add baking soda to raise the pH and add peat moss to lower the pH value. We also do check the turbidity of water using the camera and image  processing. In addition to that we propose an automated feeding system at regular intervals.

<h2>Project Scope</h2>
<p>This project will focus on developing a pH meter using an analog pH meter, conversion module and Arduino for pH monitoring. For turbidity monitoring, we use camera module and cover software parts.
This project will include,
<ul>
<li>pH monitoring system using Analog pH sensor, BNC connector which is connected to the raspberry pi 3 B+ and display the real time output to the LCD showing current pH value and the range of the suitable pH value. When the pH value changes out of the range the display will output a message saying that 
the pH out of range on the android app.</li>
<li>Turbidity checking system which uses a omni vision 5647 5MP camera module, image processing to check the turbidity and notify when to change the water by push notification</li>
<li>Automatic feeding system which feed the fish at regular intervals using the servo motor, small container, ultrasonic sensor. The ultrasonic sensor is used to check the amount feed that is available and use the same notification system to communicate with the owner when the feed is low. Servo motor will operate at regular intervals using the time of raspberry pi which is connected to the internet as raspberry pi 3 B+ already have an in-built WIFI.</li>
</ul>
<h3>Operating Environment</h3>
<img src="https://user-images.githubusercontent.com/77115237/190553010-fe8954f2-1ebe-496d-b03d-0f732ae6d988.png" width="70%" height = "auto">

<br>
<br>
<table border="0">
  <tr>
   <td>System</td>
   <td><img src="https://user-images.githubusercontent.com/77115237/190554880-4598371d-eceb-4ad2-842f-b2d638db9103.jpeg" width="30%" height = "auto"></td>
  </tr>
   <tr>
    <td>Android App</td>
   <td><img src="https://user-images.githubusercontent.com/77115237/190553570-9ff4d0e2-af69-43d8-aa01-7ae7c214f7b0.jpg" width="30%" height = "auto"></td>
  </tr>
 <tr>
    <td>Feeding Bottle</td>
    <td><img src="https://user-images.githubusercontent.com/77115237/190554664-9764c945-b465-4d56-99ea-df4819750b07.jpg" width="30%" height = "auto"></td>
 </tr>

</table>

Our system mainly contains three main parts
1. pH monitoring system
2. Turbidity monitoring
3. Automated Feeding system

All are monitored and displayed through the android app 

<h3>pH monitoring system</h3>
We use the pH probe with BNC electrode to measure the pH value. We use arduino UNO to get the readings as the pH module produces analog output. We cannot connect the pH sensor kit with the raspberry Pi. Our whole system is intergrated with Raspberry Pi and this is the only component that cannot be connected with the RPi. So we read using the Arduino UNO board and then send the values to the raspberry Pi using serial communication. Before starting the rreadings we need to calibrate the pH sensor with the provided pH solutions in order to aquire a higher accuray. I have attached the connections and the code to read using the arduino and recieve through the RPi. 
I hava attached necessary photos also.

<h3>code for measuring the pH value...</h3>

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
 
 
<h3>code for voltage calibration of the pH sensor</h3>

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
