import board
import time
import busio as io
import adafruit_mlx90614 as mlx

i2c = io.I2C(board.SCL, board.SDA, frequency=100000)
lec = mlx.MLX90614(i2c)

while True:
	text = lec.ambient_temperature
	tuser = lec.object_temperature

	print("""\nTemp Ambiente: {0:0.1f} °C\nTemp Objeto:   {1:0.1f} °C""".format(text, tuser))
	time.sleep(3)
