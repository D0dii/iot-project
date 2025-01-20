from django.urls import path
from .views import MQTTMessageList

urlpatterns = [
    path('messages/', MQTTMessageList.as_view(), name='mqtt_message_list'),
]
