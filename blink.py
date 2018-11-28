#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

LedPin = 11    # pin11

def setup():
	GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
	GPIO.setup(LedPin, GPIO.OUT)   # Set LedPin's mode is output
	GPIO.output(LedPin, GPIO.HIGH) # Set LedPin high(+3.3V) to off led

def loop(distance):
	while True:
		okres = 0.5 / distance
		print '...led on'
		GPIO.output(LedPin, GPIO.LOW)  # led on
		time.sleep(okres)
		print 'led off...'
		GPIO.output(LedPin, GPIO.HIGH) # led off
		time.sleep(okres)
def light_on():
	print "ON"
	GPIO.output(LedPin, GPIO.LOW)  # led on
	
def light_off():
	print "OFF"
	GPIO.output(LedPin, GPIO.HIGH)  # led on

def destroy():
	GPIO.output(LedPin, GPIO.HIGH)     # led off
	GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
	setup()
	try:
		loop()
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destroy()
