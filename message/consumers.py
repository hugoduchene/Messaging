from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from user.models import CustomUser
import json


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['id_conversation']
        self.room_group_name = 'message_%s' % self.room_name

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        user = text_data_json['id_user']

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'id_user': user,
            }
        )

    def chat_message(self, event):
        message = event['message']
        user = event['id_user']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message,
            'id_user': user,
        }))


class UserConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['id_user']
        self.room_group_name = 'message_%s' % self.room_name

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        send = text_data_json['send']

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'send': send,
            }
        )

    def chat_message(self, event):
        send = event['send']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'send': send,
        }))
