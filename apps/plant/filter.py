from django_filters import rest_framework as filter

from .models import PlantModel,CategoryModel,CharacterPlantModel

class CategoryFilter(filter.FilterSet):
    class Meta:
        model = CategoryModel
        fields = {
            "title": ("istartswith", "iendswith", "icontains"),
        }
    order = filter.OrderingFilter(
        fields=(
            "id",
            "title",
        )
    )



class PlantFilter(filter.FilterSet):
    is_active = filter.BooleanFilter()
    is_user_create = filter.BooleanFilter()
    category = filter.ModelChoiceFilter(
        queryset=CategoryModel.objects.all()
    )
    character_plant = filter.ModelChoiceFilter(
        queryset=CharacterPlantModel.objects.all()
    )
    category_title = filter.CharFilter(
        field_name="category__title",
        lookup_expr="icontains"
    )

    class Meta:
        model = PlantModel
        fields = {
            "crop": ("istartswith", "iendswith", "icontains"),
            "variety": ("istartswith", "iendswith", "icontains"),
            "description": ("istartswith", "iendswith", "icontains"),
            "category": ("exact",),
            "character_plant": ("exact",),
            "owner": ("exact",),
        }

    order = filter.OrderingFilter(
        fields=(
             "id",
            "crop",
            "variety",
            "is_active",
            "is_user_create",
            "category",
            "character_plant",
        )
    )

