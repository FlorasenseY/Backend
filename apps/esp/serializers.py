from rest_framework.serializers import ModelSerializer
from .models import EspContainerEspModel, UserParamsModel, SensorDeviceModel
from rest_framework import serializers


class UserParamsSerializer(ModelSerializer):
    class Meta:
        model = UserParamsModel
        fields = ('id', 'need_temp', 'need_air_humidity','need_ground_humidity','need_light', 'need_meta_params')


class SensorDeviceSerializer(ModelSerializer):
    class Meta:
        model = SensorDeviceModel
        fields = ('id', 'current_temp', 'current_air_humidity','current_ground_humidity','current_light', 'current_meta_params')


class EspContainerSerializer(ModelSerializer):
    sensor = SensorDeviceSerializer()
    user_params = UserParamsSerializer()
    class Meta:
        model = EspContainerEspModel
        fields = ('id', 'plant', 'sensor', 'user_params')




class SensorDeviceEspSerializer(serializers.Serializer):
    current_temp = serializers.IntegerField()
    current_air_humidity = serializers.IntegerField()
    current_ground_humidity = serializers.IntegerField()
    current_light = serializers.BooleanField()
    current_meta_params = serializers.JSONField()
