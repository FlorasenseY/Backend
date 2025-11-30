from django.urls import path
from .views import CreateContainerApi, RetrieveUpdateDestroyContainerApi,ListContainerApi

urlpatterns = [
    path('create/<int:pk>/', CreateContainerApi.as_view()),
    path('list/', ListContainerApi.as_view()),
    path('container/<int:pk>/', RetrieveUpdateDestroyContainerApi.as_view())
]
