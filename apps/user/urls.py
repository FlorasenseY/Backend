from django.urls import path
from .views import CreateListUserApi, RetrieveUpdateDestroyUserApi, RetrieveUpdateDestroyAdminDeviceApi, CreateSuperuserOnlyDev


urlpatterns =[
    path('register/', CreateListUserApi.as_view()),
    path('device/', RetrieveUpdateDestroyUserApi.as_view()),
    path('device/admin/<int:pk>/', RetrieveUpdateDestroyAdminDeviceApi.as_view()),
    path("device/admin/set/",  CreateSuperuserOnlyDev.as_view())
]
