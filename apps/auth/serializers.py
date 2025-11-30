from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainSerializer,RefreshToken
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.models import AbstractBaseUser, update_last_login

class TokenObtainSerializerCustom(serializers.Serializer):
    username_field = get_user_model().USERNAME_FIELD
    token_class = None

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields[self.username_field] = serializers.CharField(write_only=True)


    def validate(self, attrs):
        authenticate_kwargs = {
            self.username_field: attrs[self.username_field],
            "password": attrs[self.username_field],
        }
        try:
            authenticate_kwargs["request"] = self.context["request"]
        except:
            pass

        self.user = authenticate(**authenticate_kwargs)
        return {}

    @classmethod
    def get_token(cls, user):
        return cls.token_class.for_user(user)

class TokenObtainPairSerializerCustom(TokenObtainSerializerCustom):
    token_class = RefreshToken

    def validate(self, attrs):
        data = super().validate(attrs)
        try:
            refresh = self.get_token(self.user)
        except:
            raise serializers.ValidationError({"detail":"oops"})
        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)
        update_last_login(None, self.user)
        return data
