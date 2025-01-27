import paho.mqtt.client as mqtt
from django.utils.timezone import now

MQTT_BROKER = "10.108.33.125"
MQTT_PORT = 1883
MQTT_TOPIC = "vote"

def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT Broker with result code: " + str(rc))
    client.subscribe(MQTT_TOPIC)

def on_message(client, userdata, msg):
    message = msg.payload.decode()
    print(f"Received message: {message}")


def start_mqtt_client():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    
    client.connect(MQTT_BROKER, MQTT_PORT, 60)
    
    client.loop_start()
