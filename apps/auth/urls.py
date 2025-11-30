from django.urls import path
from rest_framework_simplejwt.views import  TokenRefreshView
from .views import LoginApi,GetMeApi

urlpatterns = [
    path("login/", LoginApi.as_view(), name="login"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("me/", GetMeApi.as_view())
]
