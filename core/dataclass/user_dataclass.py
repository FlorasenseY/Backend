from dataclasses import dataclass
from .esp_dataclass import EspContainerDataClass

@dataclass
class UserDataClass:
    id:int
    username:str
    name:str
    password:str
    is_active:bool
    is_block:bool
    is_superuser:bool
    container: EspContainerDataClass

