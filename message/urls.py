from django.urls import path
from message.views import MessageView, MessageStart

urlpatterns = [
    path('', MessageStart.as_view(), name="messagestart"),
    path('<int:id_conversation>', MessageView.as_view(), name="message")
]
