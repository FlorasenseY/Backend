from rest_framework.generics import GenericAPIView, UpdateAPIView
from .serializers import EspContainerSerializer, UserParamsSerializer
from rest_framework.permissions import IsAuthenticated
from apps.plant.models import PlantModel
from django.db.models import Q
from rest_framework import serializers
from core.dataclass import PlantDataClass, UserDataClass, EspContainerDataClass
from core.services.esp_container import set_params
from rest_framework.response import Response
from rest_framework import status

class SetPlantByContainerApi(GenericAPIView):
    serializer_class = EspContainerSerializer
    permission_classes= (IsAuthenticated,)

    def get_object(self):
        pk:int= self.kwargs.get('pk')
        user = self.request.user
        plant:PlantDataClass = PlantModel.objects.filter(id=pk).filter(Q(is_default=True) | Q(owner=user)).first()
        if plant:
            return plant
        raise serializers.ValidationError({'detail':'Plant not found'})


    def get(self, *args, **kwargs):
        user:UserDataClass = self.request.user
        plant: PlantDataClass = self.get_object()
        container:EspContainerDataClass = user.container
        container.plant = plant
        container = set_params(container, plant)
        container.save()
        return Response(EspContainerSerializer(container).data, status=status.HTTP_200_OK)



class UpdateUserParamsApi(UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserParamsSerializer

    def get_object(self):
        user:UserDataClass = self.request.user
        return user.container.user_params
