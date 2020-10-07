from django.urls import path
from .views import SearchUser


urlpatterns = [
    path('searchuser/', SearchUser.as_view(), name="searchuser")
]
