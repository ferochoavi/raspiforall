import board
import digitalio as dio
import time

ldr = dio.DigitalInOut(board.D17)
leduno = dio.DigitalInOut(board.D5)
leddos = dio.DigitalInOut(board.D6)
ledtre = dio.DigitalInOut(board.D13)
ledcua = dio.DigitalInOut(board.D19)
ledcin = dio.DigitalInOut(board.D26)

def sensor_ldr (ldr):
	count = 0
	
	ldr.direction = dio.Direction.OUTPUT
	ldr.value = False
	time.sleep(0.1)
	ldr.direction = dio.Direction.INPUT
	
	while (ldr.value == False):
		count += 1
	
	return count

def enc_leds():
	
	signal = sensor_ldr(ldr)
	
	leduno.direction = dio.Direction.OUTPUT  
	leddos.direction = dio.Direction.OUTPUT  
	ledtre.direction = dio.Direction.OUTPUT  
	ledcua.direction = dio.Direction.OUTPUT  
	ledcin.direction = dio.Direction.OUTPUT  
	
	leduno.value = False
	leddos.value = False
	ledtre.value = False
	ledcua.value = False
	ledcin.value = False
	
	if signal > 500:
		leduno.value = True
	elif signal <= 500 and signal > 400:
		leduno.value = True
		leddos.value = True
	elif signal <= 400 and signal > 300:
		leduno.value = True
		leddos.value = True
		ledtre.value = True	
	elif signal <= 300 and signal > 200:
		leduno.value = True
		leddos.value = True
		ledtre.value = True
		ledcua.value = True
	elif signal < 200:
		leduno.value = True
		leddos.value = True
		ledtre.value = True
		ledcua.value = True
		ledcin.value = True
		
	
try:
	while True:
		enc_leds()
except KeyboardInterrupt:
	pass
