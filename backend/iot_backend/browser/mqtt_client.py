import paho.mqtt.client as mqtt
from django.utils.timezone import now
from .models import Question, User, UserAnswer

MQTT_BROKER = "10.108.33.125"
MQTT_PORT = 1883
MQTT_TOPIC = "vote"
MQTT_TOPIC2 = "vote2"

client = mqtt.Client()

def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT Broker with result code: " + str(rc))
    client.subscribe(MQTT_TOPIC)
    client.subscribe(MQTT_TOPIC2)


def on_message(client, userdata, msg):
    message = msg.payload.decode()
    [rfid, vote, question_id, topic] = message.split("-")
    user = User.objects.get(rfid=rfid)
    question = Question.objects.get(pk=question_id)
    if(question.is_active != True):
        publish_message(client, topic, "-2")
        return
    
    user_answer = UserAnswer(user=user, question=question, answer=vote, created_at=now())
    user_answer.save()
    print(f"Received message: {message}")
    publish_message(client, topic, "-1")

def publish_message(client, topic, message):
    client.publish(topic, message)
    print(f"Published message: '{message}' to topic: '{topic}'")



def start_mqtt_client():
    client.on_connect = on_connect
    client.on_message = on_message
    
    client.connect(MQTT_BROKER, MQTT_PORT, 60)
    
    client.loop_start()
