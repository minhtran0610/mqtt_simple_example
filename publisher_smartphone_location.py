import paho.mqtt.client as mqtt
from random import uniform
import time

mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("Smartphone_Location")
client.connect(mqttBroker, 1883, 60)

while True:
    randNumber = uniform(0, 50)
    client.publish("DISTANCE", randNumber)
    print("The distance from home is currently " + str(randNumber) + "m.")
    time.sleep(2)