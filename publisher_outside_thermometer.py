import paho.mqtt.client as mqtt
from random import uniform
import time

mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("Temperature_Outside")
client.connect(mqttBroker, 1883, 60)

while True:
    randNumber = uniform(23.0, 27.0)
    client.publish("TEMPERATURE", randNumber)
    print("The temperature outside is currently " + str(randNumber) + " degrees Celsius.")
    time.sleep(2)