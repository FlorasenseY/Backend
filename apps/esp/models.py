from django.db import models
from apps.container.models import ContainerModel
from apps.user.models import UserModel


class BasePanelEspModel(models.Model):
    class Meta:
        db_table= "esp_container"

    owner = models.ForeignKey(UserModel, on_delete=models.CASCADE,related_name='esp')
    container = models.OneToOneField(ContainerModel, on_delete=models.CASCADE, related_name='esp')
    need_temp = models.IntegerField(default=0)
    need_air_humidity = models.IntegerField(default=0)
    need_ground_humidity = models.IntegerField(default=0)
    need_light = models.BooleanField(default=False)
    need_meta_params = models.JSONField(default=dict)



