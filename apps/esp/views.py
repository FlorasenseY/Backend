from django.http import HttpResponse
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
import json

def buzzer_on(request):
    channel_layer = get_channel_layer()

    async_to_sync(channel_layer.group_send)(
        "esp_group",
        {
            "type": "send_command",
            "command": "buzzer_on"
        }
    )
    return HttpResponse("Buzzer ON sent")

def buzzer_off(request):
    channel_layer = get_channel_layer()

    async_to_sync(channel_layer.group_send)(
        "esp_group",
        {
            "type": "send_command",
            "command": "buzzer_off"
        }
    )
    return HttpResponse("Buzzer OFF sent")
