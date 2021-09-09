import paho.mqtt.client as mqtt
import time

def on_message(client, userdata, message):
    message_str = message.payload.decode('utf_8')

    # Process the temperature
    if message_str == '2021-08-23 14:23:24.685991':
        pass
    else:
        temperature = float(message_str)
        print(f"The temperature outside is {message_str} degrees Celsius")
        if temperature > 25:
            print("The AC will be turned on")
        elif temperature <= 25:
            print("The AC will be turned off")

mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("Air_Conditioner")
client.connect(mqttBroker, 1883, 60)

client.loop_start()
client.subscribe("TEMPERATURE")
client.on_message = on_message
time.sleep(60)
client.loop_stop()