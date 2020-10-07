from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from django.db.models import Q
from django.utils import timezone

from message.models import Conversation, Message
from user.models import CustomUser

from .pagination import MenuUserPagination, MessagePagination
from .serializers import (
    ConversationSerializer,
    MessageSerializer,
    MessageSendSerializer,
)


class ReadMessage(APIView):
    def post(self, request, format=None):
        Message.objects.filter(
            id_conversation=request.data['id_conversation']
        ).update(read=True)

        return Response("OK")


class CreateConv(APIView):

    def post(self, request, format=None):
        user = CustomUser.objects.get(pk=request.data['receipient'])
        conv = Conversation.objects.filter(
            Q(id_creator=request.user.id) | Q(id_recipient=request.user.id),
            Q(id_creator=user) | Q(id_recipient=user),
        )
        conv_is_exist = conv.count()

        if conv_is_exist > 0:
            Message.objects.filter(
                id_conversation=conv[0]
            ).update(read=True)
            return Response({
                "id": conv[0].id
            })
        else:
            new_conv = Conversation(
                id_creator=request.user,
                id_recipient=user,
            )
            new_conv.save()
            serializer = ConversationSerializer(new_conv, many=False)
            return Response(serializer.data)


class InsertMessage(APIView):
    def post(self, request, format=None):
        request.data['id_giving'] = request.user.id
        serializer = MessageSerializer(data=request.data)

        if serializer.is_valid():
            conv = Conversation.objects.get(
                pk=request.data['id_conversation']
            )
            conv.last_update = timezone.now()
            conv.save()
            serializer.save()

            return Response(serializer.data)


class PaginationMessage(ListAPIView):
    serializer_class = MessageSerializer
    permission_classes = (IsAuthenticated,)
    pagination_classes = PageNumberPagination

    def get_queryset(self):
        self.pagination_class = MessagePagination
        queryset = Message.objects.filter(
            Q(id_giving=self.request.user.id) | Q(id_receiving=self.request.user.id),
            id_conversation=self.kwargs['idConversation'],
        ).order_by('date_message')

        return queryset


class PaginationUsersendMessage(ListAPIView):
    serializer_class = MessageSendSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        self.pagination_class = MenuUserPagination

        last_conv = Conversation.objects.filter(
            Q(id_creator=self.request.user.id) | Q(id_recipient=self.request.user.id),
            last_update__isnull=False,
        ).order_by('-last_update')

        for conv in last_conv:
            last_message = Message.objects.filter(
                id_conversation=conv
            ).order_by('-date_message').first()

            if conv.id_creator.id == self.request.user.id:
                conv.image_profile = str(conv.id_recipient.image_profile)
                conv.username = conv.id_recipient.username
                conv.last_message = {
                    "content_message": last_message.content_message,
                    "read": last_message.read
                }
            else:
                conv.image_profile = str(conv.id_creator.image_profile)
                conv.username = conv.id_creator.username
                conv.last_message = {
                    "content_message": last_message.content_message,
                    "read": last_message.read
                }

        return last_conv
