from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import PlantModel, CategoryModel, CharacterPlantModel
from core.dataclass.plant_dataclass import PlantDataClass, CharacterPlantDataClass


class CharacterPlantSerializer(ModelSerializer):
    class Meta:
        model = CharacterPlantModel
        fields = ('id', 'percentage_deviation', 'temp', 'air_humidity', 'ground_humidity','light')


class CategorySerializer(ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ('id', 'title')


class PlantSerializer(ModelSerializer):
    character_plant = CharacterPlantSerializer()
    class Meta:
        model = PlantModel
        fields = ('id', 'crop','variety', 'category', 'image','character_plant','description', 'is_active', 'is_default')


    def create(self, validated_data):
        character_plant:CharacterPlantDataClass = validated_data.pop('character_plant')
        character_plant = CharacterPlantModel.objects.create(**character_plant)
        plant:PlantDataClass = PlantModel.objects.create(**validated_data, character_plant=character_plant)
        plant.save()
        return plant

