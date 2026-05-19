from django.shortcuts import render, get_object_or_404
from django.views import View

from account.models import User
from account.forms import UserLoginForm


class UserRegisterView(View):
    def get(self, request):
        return render(request, "account/register.html")


class UserLoginView(View):
    def get(self, request):
        return render(request, "account/login.html", {"form": UserLoginForm})

class UserProfileView(View):
    def get(self, request, **kwargs):
        user = get_object_or_404(User, pk=kwargs['user_id'])
        return render(request, "account/profile.html", {'user': user})
