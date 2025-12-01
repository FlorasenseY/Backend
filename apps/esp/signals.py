from django.db.models.signals import post_save
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from .models import UserParamsModel, EspContainerEspModel
from .serializers import UserParamsSerializer
from core.dataclass import UserParamsDataClass,EspContainerDataClass,UserDataClass

@receiver(post_save, sender=UserParamsModel)
def update_user_params_data(sender, instance:UserParamsDataClass, created, **kwargs):
    if not created:
        esp:EspContainerDataClass = instance.esp
        user:UserDataClass = esp.user
        channel_layer = get_channel_layer()
        serializer = UserParamsSerializer(instance)
        async_to_sync(channel_layer.group_send)(
            user.username,
            {
                "type": "user_params",
                "data":serializer.data
            }
        )


