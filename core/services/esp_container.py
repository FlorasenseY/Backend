
from apps.esp.models import EspContainerEspModel,UserParamsModel, SensorDeviceModel
from rest_framework import serializers
from core.dataclass import UserDataClass
from core.dataclass import UserParamsDataClass, SensorDeviceDataClass, EspContainerDataClass, PlantDataClass

def create_container():
    user_params:UserParamsDataClass = UserParamsModel.objects.create()
    sensor:SensorDeviceDataClass = SensorDeviceModel.objects.create()
    container:EspContainerDataClass = EspContainerEspModel.objects.create(sensor=sensor, user_params=user_params)
    return container


def set_params(container:EspContainerDataClass, plant:PlantDataClass):
    character_plant = plant.character_plant
    container.user_params.need_air_humidity = character_plant.air_humidity
    container.user_params.need_ground_humidity = character_plant.ground_humidity
    container.user_params.need_light = character_plant.light
    container.user_params.need_temp = character_plant.temp
    return container
