from dataclasses import dataclass
from .plant_dataclass import PlantDataClass

@dataclass
class SensorDeviceDataClass:
    current_temp:int
    current_air_humidity:int
    current_ground_humidity:int
    current_light:bool
    current_meta_params:dict

@dataclass
class UserParamsDataClass:
    need_temp:int
    need_air_humidity:int
    need_ground_humidity:int
    need_light:bool
    need_meta_params:dict


@dataclass
class EspContainerDataClass:
    plant: PlantDataClass
    sensor: SensorDeviceDataClass
    user_params:UserParamsDataClass

