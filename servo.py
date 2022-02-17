#!/usr/bin/env python3
#-- coding: utf-8 --
import RPi.GPIO as GPIO
import time
from env import *

#Set function to calculate percent from angle
def angle_to_percent (angle) :
    if angle > 180 or angle < 0 :
        return False

    start = 4
    end = 12.5
    ratio = (end - start)/180 #Calcul ratio from angle to percent

    angle_as_percent = angle * ratio

    return start + angle_as_percent



def feedOneTime():
    GPIO.setmode(GPIO.BOARD) #Use Board numerotation mode
    GPIO.setwarnings(False) #Disable warnings

    GPIO.setup(pwm_gpio, GPIO.OUT)
    pwm = GPIO.PWM(pwm_gpio, frequence)

    #Go at 90°
    pwm.start(angle_to_percent(0))
    time.sleep(2)

    #Finish at 180°
    pwm.ChangeDutyCycle(angle_to_percent(30))
    time.sleep(2)

    #Close GPIO & cleanup
    pwm.stop()
    GPIO.cleanup()