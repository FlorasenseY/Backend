from dataclasses import dataclass

@dataclass
class UserDataClass:
    id:int
    username:str
    name:str
    password:str
    is_active:bool
    is_block:bool
    is_superuser:bool

@dataclass
class CategoryDataClass:
    id:int
    title:str

@dataclass
class CharacterPlantDataClass:
    id:int
    percentage_deviation:int
    temp:int
    air_humidity:int
    ground_humidity:int
    light:int

@dataclass
class PlantDataClass:
    id:int
    crop:str
    variety:str
    category:CategoryDataClass
    image:str
    character_plant:CharacterPlantDataClass
    description:str
    is_active:bool
    is_default:bool
    owner:UserDataClass
