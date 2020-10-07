from rest_framework import serializers
from message.models import Conversation, Message
from user.models import CustomUser


class ConversationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conversation
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'


class MessageSendSerializer(serializers.ModelSerializer):
    image_profile = serializers.SerializerMethodField()
    username = serializers.SerializerMethodField()
    last_message = serializers.SerializerMethodField()

    def get_last_message(self, obj):
        return obj.last_message

    def get_image_profile(self, obj):
        return obj.image_profile

    def get_username(self, obj):
        return obj.username

    class Meta:
        model = Conversation
        fields = (
            'id',
            'image_profile',
            'username',
            'last_message',
        )
