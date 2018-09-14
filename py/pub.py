#!/usr/bin/env python

import time
import paho.mqtt.client as mqtt
import datetime
import random

def on_publish(msg, rc):
    if rc == 0:
        print("publish success, msg = " + msg)

def on_connect(client, userdata, flags, rc):
    print("Connection returned " + str(rc))

client = mqtt.Client(
    client_id="test_mqtt_sender",# + str(random.randint(0,10000000000)),
    clean_session=True,
    userdata=None,
    protocol= mqtt.MQTTv31
)

endpoint = "localhost"
port = 1883
user = "testuser"
pwd = "testpassword"
topic = "mqtt/test"
msg = "This is a test message"


#client.tls_insecure_set(False)
#client.tls_set(trust)
client.username_pw_set(user, pwd)
client.connect(endpoint, port, 60)
client.on_connect = on_connect
client.loop_start()
time.sleep(2)
count = 0
while count < 100:
    count = count + 1
    print("Count: " + str(count))
    rc , mid = client.publish(topic, payload=msg, qos=1) #qos
    on_publish(msg, rc)
    time.sleep(0.1)
