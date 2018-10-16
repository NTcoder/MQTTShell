#!/usr/bin/python
"""
#################################
@ Author: tarun.navadia
#################################
"""
import sys
import subprocess
import paho.mqtt.publish as publish
from uuid import getnode as get_mac
import time
import json
try:
    import paho.mqtt.client as mqtt
except ImportError:
    # This part is only required to run the example from within the examples
    # directory when the module itself is not installed.
    #
    # If you have the module installed, just use "import paho.mqtt.client"
    import os
    import inspect
    cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],"../src")))
    if cmd_subfolder not in sys.path:
        sys.path.insert(0, cmd_subfolder)
    import paho.mqtt.client as mqtt

def on_message_msgs(mosq, obj, msg):
    # This callback will only be called for messages with topics that match
    # $SYS/broker/messages/#
	print("MESSAGES: "+msg.topic+" "+str(msg.qos)+" "+msg.payload.decode("utf-8"))
	p = subprocess.Popen(msg.payload.decode("utf-8"), stdout=subprocess.PIPE, shell=True, universal_newlines=True)
	try:
		out, err = p.communicate(timeout= 5)
	except subprocess.TimeoutExpired :
		out = "Timeout occoured"
		err = None
	transmitMessage = {
	"output" : str(out),
	"error" : str(err)
	}
	time.sleep(0.5)
	publish.single(mac + "/stdout", json.dumps(transmitMessage) , hostname=address)
	#publish.single(mac + "/stderror"  ,str(err) , hostname=address)
	print (out)
	print (err)

mac = str(get_mac())
mqttc = mqtt.Client(client_id=mac)

# Add message callbacks that will only trigger on a specific subscription match.
mqttc.message_callback_add(mac + "/stdin", on_message_msgs)
#mqttc.message_callback_add("#", on_message_bytes)
#mqttc.on_message = on_message

#mqttc.username_pw_set()
#print(mac)
address = "192.168.1.44" # your public/private MQTT Broker ip address
time.sleep(0.1)
mqttc.connect(address, 1883, 60)
print("Connected to :",address) 
mqttc.subscribe(mac + "/stdin", 0)
print("Subscribed to :",mac)

mqttc.loop_forever()
