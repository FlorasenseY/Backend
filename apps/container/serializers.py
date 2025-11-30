from rest_framework.serializers import ModelSerializer
from .models import ContainerModel
from apps.user.serializers import UserSerializer
from apps.plant.serializers import PlantSerializer
from rest_framework import serializers

class ContainerSerializer(ModelSerializer):
    owner = UserSerializer(read_only=True)
    plant = PlantSerializer(read_only=True)
    class Meta:
        model = ContainerModel
        fields = ('id','name', 'owner', 'plant', 'current_temp', 'current_air_humidity', 'current_ground_humidity', 'current_light', 'current_meta_params')



