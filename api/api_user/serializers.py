from rest_framework import serializers
from user.models import CustomUser


class SearchUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'image_profile', 'id')
