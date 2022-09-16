# Fish ank Monitoring System

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
