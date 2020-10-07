from django.shortcuts import render
from django.views.generic.base import View
from message.models import Conversation
from django.shortcuts import get_object_or_404
from django.db.models import Q

# Create your views here.


class MessageView(View):
    def get(self, request, id_conversation, *args, **Kwargs):
        user = get_object_or_404(
            Conversation,
            Q(id_creator=request.user.id) | Q(id_recipient=request.user.id),
            id=id_conversation,
        )

        if user.id_creator == request.user:
            infos_user = user.id_recipient
        else:
            infos_user = user.id_creator

        return render(request, 'message/message.html', context={
            'id_user': request.user.id,
            'infos_user': infos_user,
        })


class MessageStart(View):
    def get(self, request, *args, **Kwargs):
        return render(request, 'message/message_start.html', context={
            'id_user': request.user.id,
        })
