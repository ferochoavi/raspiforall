import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD) 

pin = 11

def rc_time (pin):
	count = 0
	
	gpio.setup(pin, gpio.OUT)
	gpio.output(pin, gpio.LOW)
	time.sleep(0.1)
	
	gpio.setup(pin, gpio.IN)
	
	while (gpio.input(pin) == False:
		count += 1
	
	return count
try:
	while True:
		print(rc_time(pin))
except KeyboardInterrupt:
	pass	
finally:
	gpio.cleanup()
