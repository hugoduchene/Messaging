from django.urls import path
from django.contrib.auth import views as auth_views
from user.views import (
    ConnexionView,
    RegistrerView,
)

urlpatterns = [
    path('login/', ConnexionView.as_view(), name="login"),
    path('registrer/', RegistrerView.as_view(), name="registrer"),
    path('logout', auth_views.LogoutView.as_view(next_page='/user/login'), name='logout'),

]