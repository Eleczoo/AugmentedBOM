#Programm on the wemos, measure a temp and humidity and send it through mqtt
from umqtt.simple import MQTTClient
import network
import time
import dht

#GLOBAL VARIABLES
#clientName = "ESP8266-1"
clientName = "ESP8266-CUISINE"
#clientName = "ESP8266-3"
brokerIP = "192.168.1.132"
topics = 
["veyrier/cuisine/tempHumi",
"veyrier/salon/tempHumi",
"veyrier/salleManger/tempHumi",
"veyrier/chambreJonas/tempHumi",
"veyrier/bunker/tempHumi",
"veyrier/chambreGab/tempHumi",
"veyrier/chambrePap/tempHumi",
"veyrier/chambreHugo/tempHumi",
"veyrier/chambreGab2/tempHumi",
]

def do_connect():
	import network
	sta_if = network.WLAN(network.STA_IF)
	if not sta_if.isconnected():
		print('connecting to network...')
		sta_if.active(True)
		sta_if.connect('STIRNEMANN', 'mafillesappellegabrielle')
		while not sta_if.isconnected():
			pass
	print('Connected | network config:', sta_if.ifconfig())

def publish(temp, humi):
	#message = str("Temp: {0} °C | Humi: {1} %".format(temperature, humidity))
	c = MQTTClient(clientName, brokerIP)
	c.connect()
	c.publish(topic.encode(), "{0},{1}".format(temp, humi).encode())
	c.disconnect()

do_connect()

d = dht.DHT11(machine.Pin(4))

while True:
	try:
		d.measure()
		time.sleep_ms(500)
		publish(d.temperature(), d.humidity())
		print("Temp and Humidity published in {0}".format(topic))
	except:
		pass
	time.sleep(300)


