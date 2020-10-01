from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from user.forms import (
    RegistrationForm,
    CustomUserForm,
)

# Create your views here.

""" Views to login and registrer a user """


class ConnexionView(LoginView):
    template_name = "user/login.html"
    authentication_form = CustomUserForm


class RegistrerView(View):

    def get(self, request, *args, **Kwargs):
        return render(request, "user/registrer.html", context={
            'form': RegistrationForm,
        })

    def post(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            user = authenticate(
                request,
                username=username,
                password=password1
            )
            login(request, user)

        return render(request, "user/registrer.html", context={
            'form': RegistrationForm,
        })
