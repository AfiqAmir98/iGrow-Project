from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async

from .models import DataRT

import json


class DashConsumer(AsyncWebsocketConsumer):
    @database_sync_to_async
    def create_data(self, data):
        new_data = DataRT.objects.create(data=data)
        new_data.save()
        return new_data

    async def connect(self):
        self.groupname = 'dashboard'
        await self.channel_layer.group_add(
            self.groupname,
            self.channel_name,
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.groupname,
            self.channel_name
        )

    async def receive(self, text_data):
        datapoint = json.loads(text_data)
        val = datapoint['value']

        await self.channel_layer.group_send(
            self.groupname,
            {
                'type': 'deprocessing',
                'value': val
            }
        )

        print('>>>>', text_data)

        # pass

    async def deprocessing(self, event):
        valOther = event['value']
        new_data = await self.create_data(valOther)
        await self.send(text_data=json.dumps({'value': new_data.data}))
