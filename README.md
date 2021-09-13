Software Engineering - RFID Chip Reader
Team: Ignacio Flores, JohnPaul Flores

Disclaimer:
Before the creation of this document we have discussed the path of where this project is heading. We went from using microcontrollers to ping phones to count every student who enters the building. However it was discussed that a project this big was too much for little time and resources available, for it needed multiple microcontrollers. The main reason for a project change was the decrease of microcontrollers needed and maintainability.

Key:
Blue: Important
Green: Optional


Progress entries 

JohnPaul F. @09:25 - 8/30/21
	
Microchip capability requirements
Arduino/Raspberry PI
needs a way to locate Room in building or take user input
needs to know room capacity
store student card data

Web Page requirements
The webpage has to show the following information
- location of which the rfid chip reader is at
- capacity of the room it is currently in
- number of students in the room
- which students are in the room
- students vs capacity

Notes
The webpage must be able to connect to the internet/webpage. Unsure if AJAX is appropriate
Certain Arduinos have capability for ajax
ESP8266 gives microcontrollers WiFi access
ESP8226 is compatible with arduino & Raspberry PI for around $7.00
Arduino UNO and Raspberry PI are acquired. Multiple Raspberry PI’s but one Arduino
:3
As the end of the entry, It is so far using Waterfall Model
We also need to think on how the user can update cards as the class roster changes and or room





Iggy Flores - 5:39 PM - 8/30/2021

	Resources
https://ubuntu.com/tutorials/install-and-configure-apache#1-overview
Temp installation on a ubuntu Os instead on on an Raspberry OS.

JohnPaul Flores - @0919 - 9/1/21
	Ignacio has chosen a raspberry PI 4 to be chosen for the microcontroller. Capabilities include:
Broadcom BCM2711, Quad core Cortex-A72 (ARM v8) 64-bit SoC @ 1.5GHz
2GB, 4GB or 8GB LPDDR4-3200 SDRAM (depending on model)
2.4 GHz and 5.0 GHz IEEE 802.11ac wireless, Bluetooth 5.0, BLE
Gigabit Ethernet
2 USB 3.0 ports; 2 USB 2.0 ports.
Raspberry Pi standard 40 pin GPIO header (fully backwards compatible with previous boards)
2 × micro-HDMI ports (up to 4kp60 supported)
2-lane MIPI DSI display port
2-lane MIPI CSI camera port
4-pole stereo audio and composite video port
H.265 (4kp60 decode), H264 (1080p60 decode, 1080p30 encode)
OpenGL ES 3.1, Vulkan 1.0
Micro-SD card slot for loading operating system and data storage
5V DC via USB-C connector (minimum 3A*)
5V DC via GPIO header (minimum 3A*)
Power over Ethernet (PoE) enabled (requires separate PoE HAT)
Operating temperature: 0 – 50 degrees C ambient
* A good quality 2.5A power supply can be used if downstream USB peripherals consume less than 500mA in total.
Notes.
All bullets that are bolded are capabilities of interest. Raspberry pi 3 has wifi inbuilt so during this time (0930 - 9/1/21) I will assume raspberry pi 4 has the same capability. Also the RC522 has been the rfid module of interest at this time. IMPORTANT: any tags used with this module must operate on 13.56MHZ frequency. Furthermore, the implementation for using this module requires python. I believe the team (Ignacio and JohnPaul Flores at the time of 0942 9-1-21) is proficient in python.

Iggy Flores - 1:43AM - 9/8/2021

	Resources
https://www.siteground.com/tutorials/php-mysql/connect-database/
https://projects.raspberrypi.org/en/projects/lamp-web-server-with-wordpress/2

Why were you up so late XD -jp

JohnPaul Flores - 0913 - 9/8/21

News of the raspberry PI arriving was received yesterday
As of 0918 9/8/21, there is a classmate who needs a team. We can pick him up if we so desire. We are in class so I am not sure how ignacio feels
We need 5 functions per team member. Here is a short list
	
Functions:
Integrating the rfid reader into raspberry pi (hardware)
Integrating the rfid reader into raspberry pi (software)

Display alternatives such as just a monitor or webpage

Implement a location system for the raspberry pi
Make the data base or the technique on how we shall store card ID data.
Make a sort or order of arrangement of said data (requires data structures and some theory of algorithms.
Design look and casing for electronics
Design user access to product
administrator access to product
Design product security for access of the product

Optional Functionality
Sound System for identification
Light system to show error or success in identification
Display alternatives such as just a monitor or webpage
	
Connecting raspberry pi to the internet to display data onto webpage (I prefer to do javascript/html/css, however ignacio does know php and if we do get another member then they may decide as well) This has multiple functions in of itself depending on requirements

Ignacio Flores 9/8/2021 12:28 PM

https://github.com/Omgiszbeast/RFID-Project/tree/main

Ignacio Flores 9/8/2021 1:25PM
Arduino RFID Website  + datasheet
https://www.viralsciencecreativity.com/post/arduino-rfid-sensor-mfrc522-tutorial

Ignacio Flores 9/8/2021
7:04Pm

*Finishing touches
	https://www.youngwonks.com/blog/Raspberry-Pi-4-Pinout
https://s3.amazonaws.com/yw.public/GPIO-diagram-Raspberry-Pi-4.png
https://www.amazon.com/%C2%AEMifare-Antenna-Proximity-13-56mhz-Arduino/dp/B00UBE1XJW/ref=asc_df_B00UBE1XJW/?tag=hyprod-20&linkCode=df0&hvadid=198072808542&hvpos=&hvnetw=g&hvrand=17614022839075465047&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1026758&hvtargid=pla-349595675488&psc=1\

Ignacio Flores 9 -8-2021 11:45pm

Important information/advice I got from a developer I have known for a really really long time. 
Watch this video when you have the chance: https://youtu.be/xftowyrp1YM
Skip to 3:10
Resources: 
https://docs.python.org/3/library/tkinter.html
https://tkdocs.com/
https://www.qt.io/
https://www.sqlite.org/index.html
https://riverbankcomputing.com/software/pyqt/intro

JohnPaul Flores 09:19 9/10/21

Are we using scrum development style?
#Iggy, Yes
