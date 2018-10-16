#!/usr/bin/python
"""
#################################
@ Author: tarun.navadia
#################################
"""
import paho.mqtt.publish as publish
import time
import json
import threading as thread
import paho.mqtt.client as mqtt

def on_message_msgs(mosq, obj, msg):
    # This callback will only be called for messages with topics that match
    # $SYS/broker/messages/#
	#print("MESSAGES: "+msg.topic+" "+str(msg.qos)+" "+msg.payload.decode("utf-8"))
	message_json = json.loads(msg.payload.decode("utf-8"))
	output = message_json['output']
	error = message_json['error']
	if (error != "None"):
		print(error)
	else :
		outputList = output.split('\n')
		for row in outputList:
			print (row)
	command = input(mac+"~$")
	publish.single(mac + "/stdin", command , hostname=address)

mac = input("Enter the client id of the remote device :")
mqttc = mqtt.Client(client_id = "DiagnosticClient")

# Add message callbacks that will only trigger on a specific subscription match.
mqttc.message_callback_add(mac + "/stdout", on_message_msgs)
#mqttc.message_callback_add("#", on_message_bytes)
#mqttc.on_message = on_message

#mqttc.username_pw_set()
#print(mac)
address = "13.90.101.85" # your public/private MQTT Broker ip address
time.sleep(0.1)
mqttc.connect(address, 1883, 60)
print("Connected to :",address) 
mqttc.subscribe(mac + "/stdout", 0)
print("Subscribed to :",mac)

mqttc.loop_start()
command = input(mac+"~$")
publish.single(mac + "/stdin", command , hostname=address)
while True :
	time.sleep(1)

	