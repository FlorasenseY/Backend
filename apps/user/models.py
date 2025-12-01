from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .manager import UserManager

class UserModel(AbstractBaseUser, PermissionsMixin):
    class Meta:
        db_table = 'auth_users'


    username = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)
    is_block = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    container = models.OneToOneField('esp.EspContainerEspModel', on_delete=models.CASCADE, related_name='user')
    USERNAME_FIELD = "username"
    objects = UserManager()






