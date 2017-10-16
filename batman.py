#!/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'Lian'

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
#GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)
GPIO.output(18, True)
GPIO.output(18, False)

def calling_batman():
    print("I am batman")
    GPIO.output(18, GPIO.HIGH)


def stop_calling_batman():
    GPIO.output(18, GPIO.LOW)
