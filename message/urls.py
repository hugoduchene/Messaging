from django.urls import path
from message.views import MessageView

urlpatterns = [
    path('<int:id_conversation>', MessageView.as_view(), name="message")
]
