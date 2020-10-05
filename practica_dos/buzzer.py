import digitalio
import board
import time
import busio as io
import adafruit_mlx90614 as mlx

i2c = io.I2C(board.SCL, board.SDA, frequency=100000)
lec = mlx.MLX90614(i2c)
buzzer = digitalio.DigitalInOut(board.D27)
buzzer.direction = digitalio.Direction.OUTPUT

def temp_lect():
	global text, tuser
	text = lec.ambient_temperature
	tuser = lec.object_temperature
	return text, tuser
	
while True:
	temp_lect()
	print("""\nTemp Ambiente: {0:0.1f} °C\nTemp Objeto:   {1:0.1f} °C""".format(text, tuser))
	if tuser > 37:
		buzzer.value = True
		time.sleep(0.1)
		buzzer.value = False
		time.sleep(0.01)
		buzzer.value = True
		time.sleep(0.1)
		buzzer.value = False
	elif tuser == 36 or tuser == 37:
		buzzer.value = True
		time.sleep(0.1)
		buzzer.value = False
	time.sleep(3)
