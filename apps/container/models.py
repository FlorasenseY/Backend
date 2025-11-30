from django.db import models
from apps.user.models import UserModel
from apps.plant.models import PlantModel



class ContainerModel(models.Model):
    class Meta:
        db_table = 'container'
    name = models.CharField(max_length=255, blank=True, null=True)
    owner  = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name="container")
    plant = models.ForeignKey(PlantModel, on_delete=models.CASCADE, related_name="container")
    current_temp = models.IntegerField(default=0)
    current_air_humidity = models.IntegerField(default=0)
    current_ground_humidity = models.IntegerField(default=0)
    current_light = models.BooleanField(default=False)
    current_meta_params = models.JSONField(default=dict)

