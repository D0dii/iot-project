from django.apps import AppConfig
import threading
import os

class MqttMessagesConfig(AppConfig):
    name = 'mqtt_messages'

    def ready(self):
        # Import and start the MQTT client in a separate thread
        if os.environ.get('RUN_MAIN') == "true":

            from .mqtt_client import start_mqtt_client

            threading.Thread(target=start_mqtt_client, daemon=True).start()
