from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from apps.user.serializers import UserSerializer

class LoginApi(TokenObtainPairView):


    def post(self, request, *args, **kwargs):
        print(request.data)
        return super().post(request, *args, **kwargs)


class GetMeApi(GenericAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    def get(self, *args, **kwargs):
        user = self.request.user
        return Response(UserSerializer(user).data, status=status.HTTP_200_OK)

