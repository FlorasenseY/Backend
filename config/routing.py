from django.urls import path
from apps.esp.consumers import ESPConsumer
websocket_urlpatterns = [
    path('ws/esp/', ESPConsumer.as_asgi()),
]
