from django.shortcuts import render, get_object_or_404
from django.template.context_processors import request
from django.views import View

from account.forms import UserLoginForm
from account.models import User


class UserRegisterView(View):
    def get(self, request):
        return render(request, "account/register.html")


class UserLoginView(View):
    def get(self, request):
        return render(request, "account/login.html", {"form": UserLoginForm})


class UserProfileView(View):
    def get(self, request, **kwargs):
        profile_user = request.user if request.user.pk == kwargs['user_id'] else  get_object_or_404(User, pk=kwargs['user_id'])
        return render(request, "account/profile.html", {'user': profile_user})
