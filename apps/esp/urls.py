from django.urls import path
from .views import buzzer_off, buzzer_on, CreateBaseEspContainerApi

urlpatterns = [
    path('buzzerOff/', buzzer_off),
    path('buzzerOn/', buzzer_on),
    path('set_container/<int:pk>/', CreateBaseEspContainerApi.as_view())
]
