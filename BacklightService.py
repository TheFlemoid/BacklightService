#!/usr/bin/python3

import RPi.GPIO as GPIO 
import time
import calendar
import datetime

from time import sleep

earlyTimeString = "07:00:00"
lateTimeString  = "20:00:00"

GPIO.setwarnings(False) 
 
GPIO.setmode(GPIO.BCM) 
GPIO.setup(19, GPIO.IN)
GPIO.setup(26, GPIO.OUT) 

while True:
    now = datetime.datetime.now()

    # Converting the early and late time Strings to be the current date
    earlyTimeNowString = now.strftime("%Y-%m-%d") + " " + earlyTimeString
    lateTimeNowString = now.strftime("%Y-%m-%d") + " " + lateTimeString

    earlyTime = time.strptime(earlyTimeNowString, "%Y-%m-%d %H:%M:%S")
    lateTime = time.strptime(lateTimeNowString, "%Y-%m-%d %H:%M:%S")

    earlyDateTime = datetime.datetime(1970, 1, 1) + datetime.timedelta(seconds=calendar.timegm(earlyTime))
    lateDateTime = datetime.datetime(1970, 1, 1) + datetime.timedelta(seconds=calendar.timegm(lateTime))

    if (now < earlyDateTime or now > lateDateTime):
        sleep(0.5)
        #LEDs should be active
        if GPIO.input(19) == 1:
            GPIO.output(26, True)
        else:
            GPIO.output(26, False)
    else:
        #LEDs should not be active
        GPIO.output(26, False)
        sleep(10)

