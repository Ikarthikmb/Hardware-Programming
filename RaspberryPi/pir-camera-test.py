#Code for Capturing Strangers:

from gpiozero import MotionSensor
from picamera import PiCamera
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pir=MotionSensor(23)
camera=PiCamera()
camera.rotation = 180
camera.start_preview()

while True:
	GPIO.setup(24, GPIO.OUT)
	if pir.wait_for_motion():
    	GPIO.output(24, GPIO.HIGH)
    	#time.sleep(0.1)
    	print("Motion Detected")
    	camera.capture('/home/pi/Marvel/PiCam/PiImage/Strangers/image-'+ time.ctime()+'.png')
    		print("image-"+time.ctime())
    		GPIO.output(24, GPIO.LOW)
    		
	else:
    	print("Motion not Detected")
	time.sleep(3)
camera.stop_preview()
camera.close()

