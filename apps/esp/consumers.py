from channels.generic.websocket import AsyncWebsocketConsumer
import json

class ESPConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = "esp_group"
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )

        await self.accept()
        print("Connected")


    async def disconnect(self, code):
        print("Disconnected")


    async def receive(self, text_data = None, bytes_data = None):
        data = json.loads(text_data)
        print("Receive data", data)
        await self.send(json.dumps({"status": "ok", "received": data}))

    async def send_command(self, event):
        command = event['command']
        print(f"Sending command: {command}")
        await self.send(text_data=json.dumps({"command": command}))


