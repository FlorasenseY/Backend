from django.http import HttpResponse
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
import json
from rest_framework.generics import CreateAPIView
from .serializers import BasePanelEspSerializers, BasePanelEspModel
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

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


class CreateBaseEspContainerApi(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request, *args, **kwargs):
        user = self.request.user
        container = BasePanelEspModel.objects.filter(owner = user).first()
        container_id = kwargs.get('pk')
        data= self.request.data
        serializers = BasePanelEspSerializers(data=data)
        serializers.is_valid(raise_exception=True)
        if not container:
            serializers.save(owner = user, container_id=container_id)
            return Response(serializers.data, status=status.HTTP_200_OK)
        container.container_id = container_id
        container.save()
        return Response(BasePanelEspSerializers(container).data, status=status.HTTP_200_OK)

