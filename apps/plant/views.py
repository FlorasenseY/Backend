from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import PlantSerializer, CategorySerializer, CharacterPlantSerializer
from .models import PlantModel, CategoryModel, CharacterPlantModel
from rest_framework import status
from rest_framework.permissions import IsAdminUser, AllowAny
from .filter import PlantFilter, CategoryFilter
from rest_framework.serializers import ValidationError
from rest_framework.permissions import IsAuthenticated
from core.permission.permission import IsSuperUser
from django.db.models import Q

#Plant
class CreateListPlantApi(ListCreateAPIView):
    serializer_class = PlantSerializer
    permission_classes = (IsAuthenticated,)
    filterset_class = PlantFilter

    def get_queryset(self):
        queryset = PlantModel.objects.filter(
    Q(is_default=True) | Q(owner=self.request.user)
)
        return queryset

    def perform_create(self, serializer) -> None:
        serializer.save(owner=self.request.user)

class RetrieveUpdateDestroyPlantApi(RetrieveUpdateDestroyAPIView):
    serializer_class = PlantSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return PlantModel.objects.filter(owner=self.request.user)

#Category
class CreateListCategoryApi(ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = CategoryModel.objects.all()
    filterset_class = CategoryFilter
    permission_classes = (IsSuperUser,)

class RetrieveUpdateDestroyCategoryApi(RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    permission_classes = (IsSuperUser, )
    queryset = CategoryModel.objects.all()

    def perform_destroy(self, instance) -> None:
        try:
            instance.delete()
        except:
            raise ValidationError("Cannot delete: this category is used by some plants")


#CharacterPlant
class CreateListCharacterPlantApi(ListCreateAPIView):
    serializer_class = CharacterPlantSerializer
    queryset = CharacterPlantModel.objects.all()
    permission_classes = (IsSuperUser,)

class RetrieveUpdateDestroyCharacterPlantApi(RetrieveUpdateDestroyAPIView):
    serializer_class = CharacterPlantSerializer
    queryset = CharacterPlantModel.objects.all()
    permission_classes = (IsSuperUser,)

