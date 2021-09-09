This repository contains the code for a simple publisher/subscriber system. The MQTT Broker used in this system is 'mqtt.eclipseprojects.io'.

The system contains 2 publishers: An indoor thermometer publishes indoor temperature and the user's smartphone publishes his/her distance from home.

The subscribers are the air conditioner and electronic devices of the house. The air conditioner will try to keep the room temperature around 25 degrees, and the electronic devices will start operating when the user is close to home (less than 10 meters).

The figures are completely random. Due to my novice level, the system doesn't make much sense. However, this is a good first step to learn about publisher/subscriber and internet communication.