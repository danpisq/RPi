#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
import blink

PIN_TRIGGER = 18
PIN_ECHO = 16

def setup():
    GPIO.setmode(GPIO.BOARD)

   
    GPIO.setup(PIN_TRIGGER, GPIO.OUT)
    GPIO.setup(PIN_ECHO, GPIO.IN)

    GPIO.output(PIN_TRIGGER, GPIO.LOW)
    blink.setup()

def destroy():
    # led off
    GPIO.cleanup()                     # Release resource

def run():


    print "Waiting for sensor to settle"

    time.sleep(2)
    while True:
        print "Calculating distance"
    
        GPIO.output(PIN_TRIGGER, GPIO.HIGH)

        time.sleep(0.00001)

        GPIO.output(PIN_TRIGGER, GPIO.LOW)

        while GPIO.input(PIN_ECHO)==0:
            pulse_start_time = time.time()
        while GPIO.input(PIN_ECHO)==1:
            pulse_end_time = time.time()

        pulse_duration = pulse_end_time - pulse_start_time
        distance = round(pulse_duration * 17150, 2)
        if distance < 20:
            blink.light_on()
        else:
            time.sleep(0.5)
            blink.light_off()
        print "Distance:",distance,"cm"
        time.sleep(1)

if __name__ =='__main__':
    try:
        setup()
        run()
    except KeyboardInterrupt:
        blink.destroy()
