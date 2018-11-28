import RPi.GPIO as GPIO
import time

LedPin = 11
ButtonPin = 12

def setup():
	GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
	GPIO.setup(LedPin, GPIO.OUT)   # Set LedPin's mode is output
	GPIO.output(LedPin, GPIO.HIGH) # Set LedPin high(+3.3V) to off led
	GPIO.setup(ButtonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def run():
	while True:
		input_state = GPIO.input(ButtonPin)
		if input_state == False:
			print('Button Pressed')
			GPIO.output(LedPin, GPIO.LOW)  # led on
			
			
		if input_state == True:
			GPIO.output(LedPin, GPIO.HIGH)  # led off
			
	
def destroy():
	GPIO.output(LedPin, GPIO.HIGH)     # led off
	GPIO.cleanup()                     # Release resource
	
		
if __name__ == '__main__':
	setup()
	try:
		run()
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destroy()

