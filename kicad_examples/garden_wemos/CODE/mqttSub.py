#python programm on rasp receives data from mqtt protocol and put it into a database

import paho.mqtt.client as mqtt #import the client1
import sqlite3
from datetime import date
from datetime import datetime

broker_address="192.168.1.132"

topics = [("veyrier/cuisine/tempHumi", 0),
("veyrier/salon/tempHumi", 0),
("veyrier/salleManger/tempHumi", 0),
("veyrier/chambreJonas/tempHumi", 0),
("veyrier/bunker/tempHumi", 0),
("veyrier/chambreGab/tempHumi", 0),
("veyrier/chambrePap/tempHumi", 0),
("veyrier/chambreHugo/tempHumi", 0),
("veyrier/chambreGab2/tempHumi", 0),
]

def getDateTime():
	now = datetime.now()
	time = str(now.strftime("%H:%M:%S"))
	date = str(now.strftime("%d/%m/%Y"))

	return date, time


def on_message(client, userdata, message):
	print("topic=",message.topic)

	temp, humi = str(message.payload.decode("utf-8")).split(",")
	date, time = getDateTime()
	
	try:
		#création objects
		connectionDB = sqlite3.connect("TEMPHUM_WEMOS.db")
		cursorDB = connectionDB.cursor()
		new_entry = (cursorDB.lastrowid, date, time, temp, humi)

		cursorDB.execute(f'INSERT INTO {message.topic.split("/")[1]} VALUES(?,?,?,?,?)', new_entry)
		connectionDB.commit()
		print(f" written to DB, into {message.topic.split('/')[1]} table!")
	except:
		pass

	
def on_connect(client, userdata, flags, rc):
	if rc==0:
		print("connected OK Returned code=",rc)
	else:
		print("Bad connection Returned code=",rc)


client = mqtt.Client("PCtest") #create new instance
client.on_message=on_message #attach function to callback
client.on_connect=on_connect #attach function to callback

client.connect(broker_address) #connect to broker
client.subscribe(topics) #Sub to topic

client.loop_forever() #start the loop
