#!/usr/bin/python3

import RPi.GPIO as GPIO 
from time import sleep 
GPIO.setwarnings(False) 
 
GPIO.setmode(GPIO.BCM) 
GPIO.setup(19, GPIO.IN)
GPIO.setup(26, GPIO.OUT) 

while True:
    sleep(0.25)
    if GPIO.input(19) == 1:
        GPIO.output(26, True)
    else:
        GPIO.output(26, False)

