import os
import threading
from django.apps import AppConfig


class BrowserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'browser'

    def ready(self):
        if os.environ.get('RUN_MAIN') == "true":

            from .mqtt_client import start_mqtt_client

            threading.Thread(target=start_mqtt_client, daemon=True).start()
               

