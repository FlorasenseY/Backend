from django.urls import path
from .views import CreateListPlantApi, RetrieveUpdateDestroyPlantApi, CreateListCategoryApi, RetrieveUpdateDestroyCategoryApi, CreateListCharacterPlantApi, RetrieveUpdateDestroyCharacterPlantApi
urlpatterns = [
    #plant
    path('plant/', CreateListPlantApi.as_view()),
    path('plant/<int:pk>/', RetrieveUpdateDestroyPlantApi.as_view()),
    #category
    path('category/', CreateListCategoryApi.as_view() ),
    path('category/<int:pk>/', RetrieveUpdateDestroyCategoryApi.as_view()),
    #character
    path('character/', CreateListCharacterPlantApi.as_view()),
    path('character/<int:pk>/', RetrieveUpdateDestroyCharacterPlantApi.as_view()),

]
