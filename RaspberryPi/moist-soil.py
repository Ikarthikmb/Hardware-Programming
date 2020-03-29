import RPi.GPIO as GPIO
from time import sleep

import Adafruit_MCP3008

am = Adafruit_MCP3008.MCP3008(clk = 11, cs = 8, miso = 9, mosi = 10)

while True:
  moisture_value = am.read_adc(0)
  if moisture_value >= 930:
    print(" No water, Can you plaease water me")
  elif moisture_value < 930 and moisture_value >= 350:
    print(" I'm sufficient ")
  elif moisture_value < 350 :
    print(" Stop drowning me!")
  sleep(1.5)
