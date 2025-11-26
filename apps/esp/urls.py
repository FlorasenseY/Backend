from django.urls import path
from .views import buzzer_off, buzzer_on

urlpatterns = [
    path('buzzerOff/', buzzer_off),
    path('buzzerOn/', buzzer_on)
]
