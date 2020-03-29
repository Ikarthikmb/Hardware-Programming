# import pandas as pd
import numpy as np
from RPi.GPIO import GPIO

def waterval():
    # Get the water capacity from the soil sensor
    water = int(input('enter water capacity'))
    return water

def intruder():
    # Get the image from the pi cam
    if motiondetect:
        print("Taken a snap of the")

th = 120
def groot():
    while True:
        water = waterval()   # Check the level of water in the soil
        intruder()       # Detect the motion and capture the photo
        if (water < th-15):
            print("[INFO] Insufficient water")
        elif (water == th) & (water < th+15) & (water >= th-15):
            print("[INFO] Water is Good")
        elif (water > th+15):
            print("[INFO] Water is more than enough")
        else:
            return
    

groot()
