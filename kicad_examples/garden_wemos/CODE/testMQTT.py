from umqtt.simple import MQTTClient
import network
import time

def do_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('STIRNEMANN', 'mafillesappellegabrielle')
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())



def publish():
    c = MQTTClient("esp8266-2", '192.168.1.132')
    c.connect()
    c.publish(b"dossier/test1", b"message from the esp8266-2")
    c.disconnect()

do_connect()

while True:
	publish()
	time.sleep(10)
