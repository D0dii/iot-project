import paho.mqtt.client as mqtt
from .models import MQTTMessage
from django.utils.timezone import now
import threading

# MQTT Broker configuration
MQTT_BROKER = "localhost"
MQTT_PORT = 1883
MQTT_TOPIC = "buttons/press"

# MQTT Callback functions
def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT Broker with result code: " + str(rc))
    client.subscribe(MQTT_TOPIC)

def on_message(client, userdata, msg):
    message = msg.payload.decode()
    print(f"Received message: {message}")
    
    # Save the message to the database
    MQTTMessage.objects.create(message=message)

# MQTT Client setup
def start_mqtt_client():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    
    client.connect(MQTT_BROKER, MQTT_PORT, 60)
    
    client.loop_start()  # Start the MQTT loop in a separate thread
