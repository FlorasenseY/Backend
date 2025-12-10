
from apps.esp.models import EspContainerEspModel,UserParamsModel, SensorDeviceModel
from core.dataclass import UserParamsDataClass, SensorDeviceDataClass, EspContainerDataClass, PlantDataClass
from core.dataclass.plant_dataclass import CharacterPlantDataClass

def create_container() -> EspContainerDataClass:
    user_params:UserParamsDataClass = UserParamsModel.objects.create()
    sensor:SensorDeviceDataClass = SensorDeviceModel.objects.create()
    container:EspContainerDataClass = EspContainerEspModel.objects.create(sensor=sensor, user_params=user_params)
    return container


def set_params(container:EspContainerDataClass, plant:PlantDataClass) -> EspContainerDataClass:
    character_plant: CharacterPlantDataClass = plant.character_plant
    user_params: UserParamsDataClass = container.user_params
    user_params.need_air_humidity = character_plant.air_humidity
    user_params.need_ground_humidity = character_plant.ground_humidity
    user_params.need_light = True
    user_params.need_temp = character_plant.temp
    user_params.save()
    container.save()
    return container
