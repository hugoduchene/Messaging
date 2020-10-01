from django.shortcuts import render
from django.views.generic.base import View

# Create your views here.

""" Views to login a user """


class ConnexionView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "user/login.html", context=None)
