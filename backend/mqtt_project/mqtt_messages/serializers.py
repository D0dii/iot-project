from rest_framework import serializers
from .models import MQTTMessage

class MQTTMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MQTTMessage
        fields = ['id', 'message', 'received_at']
