import paho.mqtt.client as mqtt
import time

def on_message(client, userdata, message):
    message_str = message.payload.decode('utf_8')

    # Process the distance
    if message_str == '2021-08-23 14:23:24.685991':
        pass
    else:
        distance = float(message_str)
        print(f"The user is currently {message_str}m from home.")
        if distance <= 10:
            print("Time to turn on the electronic devices")

mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("Electronic_Devices")
client.connect(mqttBroker, 1883, 60)

client.loop_start()
client.subscribe("DISTANCE")
client.on_message = on_message
time.sleep(60)
client.loop_stop()