from django.db import models

class CategoryModel(models.Model):
    class Meta:
        db_table = "category"
    title = models.CharField(max_length=50, unique=True)


class CharacterPlantModel(models.Model):
    class Meta:
        db_table= "character_plant"
    percentage_deviation = models.IntegerField(default=5)
    temp =  models.IntegerField(default=24)
    air_humidity = models.IntegerField(default=60)
    ground_humidity = models.IntegerField(default=60)
    light = models.IntegerField(default=8) #per hour/day
    is_user_create = models.BooleanField(default=True)


class PlantModel(models.Model):
    class Meta:
        db_table = "plant"
    crop = models.CharField(max_length=50)
    variety = models.CharField(max_length=50)
    category: models.ForeignKey[CategoryModel] =  models.ForeignKey(CategoryModel, on_delete=models.PROTECT, related_name='plant', blank=True, null=True)
    image = models.ImageField(upload_to="plant/", null=True, blank=True)
    character_plant = models.ForeignKey(CharacterPlantModel, on_delete=models.CASCADE, related_name='plant')
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=False)
    is_default = models.BooleanField(default=False)
    owner = models.ForeignKey("user.UserModel", on_delete=models.CASCADE, related_name="plant")


