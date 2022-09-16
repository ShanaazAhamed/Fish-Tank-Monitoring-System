# Fish ank Monitoring System
Fish and other aquatic animals need a balanced pH for survival of them. This pH value can make fish sick and  even kill them. Therefore, we are proposing a system for fish tanks which monitors the value of pH using the pH  sensor and alert the specific person using notification. There after we can add baking soda to raise the pH and  add peat moss to lower the pH value. We also do check the turbidity of water using the camera and image  processing. In addition to that we propose an automated feeding system at regular intervals.

<h2>Project Scope</h2>
<p>This project will focus on developing a pH meter using an analog pH meter, conversion module and Arduino for pH monitoring. For turbidity monitoring, we use camera module and cover software parts.
This project will include,
<ul>
<li>pH monitoring system using Analog pH sensor, BNC connector which is connected to the raspberry pi 3 B+ and display the real time output to the LCD showing current pH value and the range of the suitable pH value. When the pH value changes out of the range the display will output a message saying that 
the pH out of range on the android app.</li>
<li>Turbidity checking system which uses a omni vision 5647 5MP camera module, image processing to check the turbidity and notify when to change the water by push notification</li>
<li>Automatic feeding system which feed the fish at regular intervals using the servo motor, small container, ultrasonic sensor. The ultrasonic sensor is used to check the amount feed that is available and use the same notification system to communicate with the owner when the feed is low. Servo motor will operate at regular intervals using the time of raspberry pi which is connected to the internet as raspberry pi 3 B+ already have an in-built WIFI.</li>
</ul>
</p>
