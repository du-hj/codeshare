#!/usr/bin/env python

import paho.mqtt.client as mqtt
import json
import random


endpoint = "localhost"
port = 1883
user = "testuser"
pwd = "testpassword"
topic = "mqtt/test"
keepalive = 20
topic = "mqtt/#"

count=0

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(topic, qos=1) #qos

def on_message(client, userdata, msg):
    global count
    count = count + 1
    strPayload = str(msg.payload)
    print("\nCount" + str(count) +  "\nTopic: [" + msg.topic + "]" + "\n" + strPayload)
    
client = mqtt.Client(
    client_id="test_mqtt_receiver1",# + str(random.randint(0,10000000000)),
    clean_session=False,
    userdata=None,
    protocol= mqtt.MQTTv31
)

#client.tls_insecure_set(False)
#client.tls_set(trust)
client.username_pw_set(user, pwd)
client.on_connect = on_connect
client.on_message = on_message
client.connect(endpoint,port,keepalive)
client.loop_forever()
