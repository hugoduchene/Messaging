from django.urls import path
from user.views import (
    ConnexionView,
)

urlpatterns = [
    path('login/', ConnexionView.as_view(), name="login"),
]