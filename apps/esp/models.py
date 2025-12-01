from django.db import models

class SensorDeviceModel(models.Model):
    class Meta:
        db_table = 'sensor'
    current_temp = models.IntegerField(default=0)
    current_air_humidity = models.IntegerField(default=0)
    current_ground_humidity = models.IntegerField(default=0)
    current_light = models.BooleanField(default=False)
    current_meta_params = models.JSONField(default=dict)


class UserParamsModel(models.Model):
    class Meta:
        db_table="user_params"
    need_temp = models.IntegerField(default=0)
    need_air_humidity = models.IntegerField(default=0)
    need_ground_humidity = models.IntegerField(default=0)
    need_light = models.BooleanField(default=False)
    need_meta_params = models.JSONField(default=dict)



class EspContainerEspModel(models.Model):
    class Meta:
        db_table= "esp_container"
    plant = models.OneToOneField("plant.PlantModel", on_delete=models.SET_NULL, null=True, blank=True, related_name='esp')
    sensor = models.OneToOneField(SensorDeviceModel, on_delete=models.CASCADE, related_name='esp')
    user_params= models.OneToOneField(UserParamsModel, on_delete=models.CASCADE, related_name='esp')

