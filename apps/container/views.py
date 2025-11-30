from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from .serializers import ContainerSerializer, ContainerModel
from rest_framework.permissions import IsAuthenticated


class CreateContainerApi(CreateAPIView):
    serializer_class = ContainerSerializer
    permission_classes = (IsAuthenticated,)


    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        serializer.save(owner=self.request.user, plant_id=pk)

class ListContainerApi(ListAPIView):
    serializer_class = ContainerSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return ContainerModel.objects.filter(owner=self.request.user)

class RetrieveUpdateDestroyContainerApi(RetrieveUpdateDestroyAPIView):
    serializer_class = ContainerSerializer
    permission_classes = (IsAuthenticated,)
    queryset = ContainerModel.objects.all()
