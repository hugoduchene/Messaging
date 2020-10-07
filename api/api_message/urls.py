from django.urls import path
from .views import (
    CreateConv,
    InsertMessage,
    PaginationMessage,
    PaginationUsersendMessage,
    ReadMessage,
)


urlpatterns = [
    path('createconversation/', CreateConv.as_view(), name="createconv"),
    path('insertmessage/', InsertMessage.as_view(), name="insertmessage"),
    path('messageconversation/<int:idConversation>', PaginationMessage.as_view(), name="messageconv"),
    path('lastuser', PaginationUsersendMessage.as_view(), name="lastuser"),
    path('readmessage/', ReadMessage.as_view(), name="readmessage"),
]
