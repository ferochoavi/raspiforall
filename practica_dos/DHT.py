import Adafruit_DHT as dht
import time

DHT_SENSOR = dht.DHT11
DHT_PIN = 4
 
while True:
	humidity, temperature = dht.read(DHT_SENSOR, DHT_PIN)
	if humidity is not None:
		print("Humidity: {0} %".format(humidity))
	else:
		print("Sensore failure. Check wiring.")
	time.sleep(3)
