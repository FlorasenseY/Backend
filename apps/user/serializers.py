from rest_framework.serializers import ModelSerializer
from .models import UserModel
from apps.esp.serializers import EspContainerSerializer
from core.services.esp_container import  create_container


class UserSerializer(ModelSerializer):
    container = EspContainerSerializer(read_only=True)
    class Meta:
        model = UserModel
        fields = ('id', 'username', 'name', 'is_active', 'is_block', 'is_superuser', 'container')
        read_only_fields = ('id', 'is_active', 'is_block', 'is_superuser', 'container')

    def create(self, validated_data):
        container = create_container()
        user = UserModel.objects.create_user(**validated_data,container=container)
        user.save()
        return user



class UserAdminSerializer(ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('id', 'username', 'name', 'is_active', 'is_block', 'is_superuser')


