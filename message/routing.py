from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/message/(?P<id_conversation>\w+)/', consumers.ChatConsumer),
    re_path(r'ws/messages/(?P<id_user>\w+)/', consumers.UserConsumer)
]
