from django.shortcuts import render
from django.views.generic.base import View
from message.models import Conversation
from django.shortcuts import get_object_or_404
from django.db.models import Q

# Create your views here.


class MessageView(View):
    def get(self, request, id_conversation, *args, **Kwargs):
        get_object_or_404(
            Conversation,
            Q(id_creator=request.user.id) | Q(id_recipient=request.user.id),
            id=id_conversation,
        )

        return render(request, 'message/message.html', context={
            'id_conversation': id_conversation,
            'id_user': request.user.id,
        })
