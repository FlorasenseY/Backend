from rest_framework.serializers import ModelSerializer
from .models import BasePanelEspModel


class BasePanelEspSerializers(ModelSerializer):
    class Meta:
        model = BasePanelEspModel
        fields = ('id','container',"need_temp", "need_air_humidity", "need_ground_humidity","need_light","need_meta_params",
        )
        read_only_fields = ('container',)

