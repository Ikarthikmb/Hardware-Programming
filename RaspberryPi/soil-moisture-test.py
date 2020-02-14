#Code for Soil Moisture detection:

import RPi.GPIO as GPIO
import time

#GPIO SETUP
GPIO.setwarnings(False)
channel = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)
GPIO.setup(24, GPIO.OUT)

GPIO.output(24, GPIO.LOW)

def callback(channel):
	GPIO.output(24, GPIO.LOW)
	if GPIO.input(channel):
    		print("No Water Detected!")
    		GPIO.output(24, GPIO.LOW)
      
	else:
    		print("Water Detected!")
    		GPIO.output(24, GPIO.HIGH)
            
# infinite loop
while True:
   time.sleep(2)
   callback(channel)

