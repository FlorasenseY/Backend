from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
from channels.db import database_sync_to_async
from core.dataclass import UserDataClass
from .serializers import SensorDeviceEspSerializer
import json
from .models import SensorDeviceModel
from .serializers import UserParamsSerializer
class ESPConsumer(GenericAsyncAPIConsumer):
    async def connect(self) -> None:
        self.user:UserDataClass = self.scope['user']
        if not self.scope['user']:
            return await self.close()
        await self.accept()
        self.group_name = self.user.username
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        user_params = await self.get_data()
        await self.send_json({"detail":f"Connect device {self.user.username} success"})
        await self.send_json({"backend":user_params})


    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.group_name)


    async def receive(self, text_data):
        try:
            data = json.loads(text_data)
            if not data.get('esp'):
                return
            data = data.pop('esp')
        except:
            await self.send_json({"detail":"Invalid data"})
            return
        serializer = SensorDeviceEspSerializer(data=data)
        if not serializer.is_valid():
            await self.send_json({"detail": serializer.errors})
            return

        await self.change_current_value(data)



    async def user_params(self, event):
        await self.send_json({"backend":event["data"]})

    @database_sync_to_async
    def get_data(self):
        user_params = self.user.container.user_params
        serializer = UserParamsSerializer(user_params)
        return serializer.data

    @database_sync_to_async
    def change_current_value(self,data):
        sensor = self.user.container.sensor
        for key,value in data.items():
            setattr(sensor,key, value)
        sensor.save()
