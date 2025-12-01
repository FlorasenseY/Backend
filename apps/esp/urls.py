from django.urls import path
from .views import SetPlantByContainerApi, UpdateUserParamsApi
urlpatterns = [
    path('set_plant/<int:pk>/', SetPlantByContainerApi.as_view()),
    path('params/', UpdateUserParamsApi.as_view())
]
