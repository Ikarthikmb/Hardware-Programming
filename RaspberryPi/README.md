# Contents

1. [Using Ultrasonic Sensor to Capture Positional Changes of Objects](#1-using-ultrasonic-sensor-to-capture-positional-changes-of-objects)
2. [Measuring Soil Moisture using Raspberry Pi](2-Measuring-Soil-Moisture-using-Raspberry-Pi)

- [Related Links](#related-links)

---

## 1 Using Ultrasonic Sensor to Capture Positional Changes of Objects
It is important to have your valuable things safe, it would be lame if you keep on guarding your castle the whole day. Using the raspberry pi camera you can take the snaps at the right moment. 

This guide will help you shoot a video or take the picture when the changes are sensed within the boundary area.

### Hardware:

 - Raspberry Pi 2/3/4
 - Ultrasonic sensor
 - Pi camera
 - Jumpers

### Step 1: Connections

- TRIG to RPI4B 17
- VCC to RPI4B 5V
- GND to RPI4B GND
- Echo to 470-ohm resistor to connection-1
- GND to 1K ohm resistor to connection-1
- connection-1 to RPI4B 4

The circuit schematic is made using circuito.io, it has all the most popular microcontrollers, sensors, etc and the platform is easy to use for beginners

### Step 2: Upload the Code

Before you run the script, create a folder through following commands opening the terminal and then edit the script file.
```
pi@raaspberrypi: mkdir media
pi@raaspberrypi: nano measure.py
```
The code uses camera and GPIO libraries. Cross-check the GPIO_TRIGGER & GPIO_ECHO pins are properly connected to 17th & 4th pins of the Raspberry Pi externally.

Copy and paste the below code or type into the python file and name it as 'measure.py'
```
#Libraries<br>import RPi.GPIO as GPIO
import time
import os
from picamera import PiCamera

# Camera Mode
camera = PiCamera()
camera.rotation = 180 # Comment this line if the image is perfectly angled

#GPIO Mode
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#set GPIO Pins
GPIO_TRIGGER = 17
GPIO_ECHO = 4

#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

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
 
if __name__ == '__main__':
    camera.start_preview(alpha=200)
    try:
        while True:
            dist = distance()
            print ("Measured Distance = %.1f cm" % dist)
            if dist<= 20 : # change this value according to your setting
                now = time.ctime().replace(" ", "-")
                camera.capture("media/image%s.jpg" % now)
                print("Image saved at media/image-%s.jpg" % now)
                # camera.start_recording("media/video-%s.h264" % now)    # Uncomment this to take a video
                # print("Video saved at media/image-%s.jpg" % now)
                # sleep(5) # Uncomment this to take a video for 5 seconds
            time.sleep(3)
        camera.stop_preview()
        # camera.stop_recording()     # Uncomment this to take a video
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
```

### Step 3: Run the Code

Now run the script as

    pi@raspberrypi: python measure.py

The distance is measured for every 3 seconds(you can change the value in the script) and is printed onto the screen if an object is identified within the 20 centimetres, the pi camera takes a photo and saves in the media folder.

Alternatively, you can shoot a video by uncommenting or remove the hashtags(#) from the script lines mentioned as comments. You can also extend the video length by simply incrementing/decrementing the value in “time.sleep(5)”.

Happy Circuiting!

---

## 2 Measuring Soil Moisture using Raspberry Pi

Do you know how often to water plants? Or outpoured plants and lost them. To solve this I thought it would be more circumstantial if we can get the value of water content inside the soil in order to make a decision for watering the plants appropriately.

In this project lets try to build a circuit which can measure the water content value of the soil eventually control the flow using Raspberry Pi.

### Hardware:
- Raspberry Pi 2/3/4
- Soil moisture sensor
- MCP3008
- Jumpers

### Circuit Connection:
   ![Circuit diagram](/images/soil-moist/soil-moisture-circuit.jpg)
- MCP3008 GND to GND
- MCP3008 CS to RPI 8
- MCP3008 DIN to RPI 10
- MCP3008 DOUT to RPI 9
- MCP3008  CLK to RPI 11
- MCP3008 AGND to GND
- MCP3008 VREF to +3V
- MCP3008 VCC to +3V
- SoilMoisture A0 to MCP3008 CH0
- SoilMoisture VCC to +3V
- SoilMoisture GND to GND 

Make all the connections and power up the Raspberry Pi. If you want to learn how to connect a Raspberry Pi check out how to [Set Up Raspberry Pi 4 Through Laptop/pc Using Ethernet Cable(No Monitor, No Wi-Fi)](https://www.instructables.com/id/Set-Up-Raspberry-Pi-4-Through-Laptoppc-Using-Ether/)

### Essential Packages
Before you run the code you have to install few libraries, move on with the following steps.
```
sudo apt-get update
sudo apt-get install build-essential python-dev python-smbus git
cd ~
git clone https://github.com/adafruit/Adafruit_Python_MCP3008.git
cd Adafruit_Python_MCP3008
sudo python setup.py install
```
### The Code
Once the library has been installed it's time to execute the code. Jump to the [code](https://github.com/Ikarthikmb/Hardware-Codes/blob/master/RaspberryPi/moist-soil.py)
```
import RPi.GPIO as GPIO
from time import sleep

import Adafruit_MCP3008

am = Adafruit_MCP3008.MCP3008(clk = 11, cs = 8, miso = 9, mosi = 10)

while True:
  moisture_value = am.read_adc(0)
  per = moisture_value * 100 / 1023
  print("Recorded moisture value is %s percentage" % per)
  if moisture_value >= 930:
    print(" No water, Can you plaease water me")
  elif moisture_value < 930 and moisture_value >= 350:
    print(" I'm sufficient ")
  elif moisture_value < 350 :
    print(" Stop drowning me!")
  sleep(1.5)
```

---

# Related Links

- For more information, raspberry-pi articles, projects [click here](https://sites.google.com/view/makewithraspberry/home).
- [How to Setup Raspberry Pi](https://www.instructables.com/id/Set-Up-Raspberry-Pi-4-Through-Laptoppc-Using-Ether/)
- [Using Ultrasonic Sensor to Capture Positional Changes of Objects](https://www.instructables.com/id/Using-Ultrasonic-Sensor-to-Capture-Sensitive-Chang/)

