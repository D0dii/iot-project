from rest_framework.views import APIView
from rest_framework.response import Response
from .models import MQTTMessage
from .serializers import MQTTMessageSerializer

class MQTTMessageList(APIView):
    def get(self, request):
        messages = MQTTMessage.objects.all()
        serializer = MQTTMessageSerializer(messages, many=True)
        return Response(serializer.data)
