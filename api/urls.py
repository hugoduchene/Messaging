from django.urls import path, include


urlpatterns = [
    path('user/', include('api.api_user.urls')),
    path('message/', include('api.api_message.urls')),
]