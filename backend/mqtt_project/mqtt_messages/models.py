from django.db import models

class MQTTMessage(models.Model):
    message = models.TextField()
    received_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message received at {self.received_at}: {self.message}"
