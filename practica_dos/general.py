import Adafruit_DHT as dht
import adafruit_mlx90614 as mlx
import busio as io
import digitalio as dio
import board
import time
from os import system, name
import statistics as stat

ldr = dio.DigitalInOut(board.D17)
leduno = dio.DigitalInOut(board.D5)
leddos = dio.DigitalInOut(board.D6)
ledtre = dio.DigitalInOut(board.D13)
ledcua = dio.DigitalInOut(board.D19)
ledcin = dio.DigitalInOut(board.D26)
DHT_SENSOR = dht.DHT11
DHT_PIN = 4
humedad_prom = []
i2c = io.I2C(board.SCL, board.SDA, frequency=100000)
lec = mlx.MLX90614(i2c)
buzzer = dio.DigitalInOut(board.D27)
buzzer.direction = dio.Direction.OUTPUT

def clear ():
	if True:
		_ = system('clear')

def sensor_ldr (ldr):
	count = 0
	
	ldr.direction = dio.Direction.OUTPUT
	ldr.value = False
	
	ldr.direction = dio.Direction.INPUT
	
	while (ldr.value == False):
		count += 1
	
	return count
	
def enc_leds ():
	
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
		print("Iluminación: Muy Pobre")
		leduno.value = True
	elif signal <= 500 and signal > 400:
		print("Iluminación: Pobre")
		leduno.value = True
		leddos.value = True
	elif signal <= 400 and signal > 300:
		print("Iluminación: Regular")
		leduno.value = True
		leddos.value = True
		ledtre.value = True	
	elif signal <= 300 and signal > 200:
		print("Iluminación: Buena")
		leduno.value = True
		leddos.value = True
		ledtre.value = True
		ledcua.value = True
	elif signal < 200:
		print("Iluminación: Muy Buena")
		leduno.value = True
		leddos.value = True
		ledtre.value = True
		ledcua.value = True
		ledcin.value = True

def sensor_dht ():
	humidity, temperature = dht.read(DHT_SENSOR, DHT_PIN)
	if humidity is not None:
		humedad_prom.append(humidity)
	else:
		pass
		#print("Sensore failure. Check wiring.")

def mostrar_hum ():
	if len(humedad_prom) == 0:
		print("Humedad: No value yet")
	if len(humedad_prom) < 50 and len(humedad_prom) > 0:
		prom = stat.mean(humedad_prom)
		print("Humedad: {0:0.1f}%".format(prom))
	else:
		humedad_prom.clear()
	
def temp_lect ():
	global text, tuser
	text = lec.ambient_temperature
	tuser = lec.object_temperature
	return text, tuser

def buzzer_alert ():
	temp_lect()
	print("""Temp Ambiente: {0:0.1f} °C\nTemp Objeto:   {1:0.1f} °C""".format(text, tuser))

	if tuser >= 37:
		print("Estado de Temperatura: Fiebre")
		buzzer.value = True
		time.sleep(0.1)
		buzzer.value = False
		time.sleep(0.01)
		buzzer.value = True
		time.sleep(0.1)
		buzzer.value = False
	elif tuser <37:
		print("Estado de Temperatura: Normal")
	
try:
	while True:
		sensor_dht()
		clear()
		enc_leds()
		mostrar_hum()
		buzzer_alert()
		time.sleep(1)
		
except KeyboardInterrupt:
	pass

