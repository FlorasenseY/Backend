from rest_framework.serializers import ModelSerializer
from .models import UserModel



class UserSerializer(ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('id', 'username', 'name', 'is_active', 'is_block', 'is_superuser')
        read_only_fields = ('id', 'is_active', 'is_block', 'is_superuser')




    def create(self, validated_data):
        user = UserModel.objects.create_user(**validated_data)
        user.save()
        return user



class UserAdminSerializer(ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('id', 'username', 'name', 'is_active', 'is_block', 'is_superuser')


