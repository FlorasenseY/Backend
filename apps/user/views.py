from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView,GenericAPIView
from .serializers import UserSerializer, UserAdminSerializer
from .models import UserModel
from rest_framework.permissions import IsAuthenticated
from core.permission.permission import IsSuperUser
from rest_framework.response import Response
from rest_framework import status
class CreateListUserApi(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()


class RetrieveUpdateDestroyUserApi(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    permission_classes = (IsAuthenticated,)
    def get_object(self):
        return self.request.user


#admin
class RetrieveUpdateDestroyAdminDeviceApi(RetrieveUpdateDestroyAPIView):
    serializer_class = UserAdminSerializer
    queryset = UserModel.objects.all()
    permission_classes = (IsSuperUser,)


class CreateSuperuserOnlyDev(GenericAPIView):
    def get(self, *args, **kwargs):
        admin = self.request.user
        admin.is_superuser = True
        admin.save()
        return Response(UserSerializer(admin).data, status=status.HTTP_200_OK)

