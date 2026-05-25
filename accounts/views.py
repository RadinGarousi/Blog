from django.shortcuts import render, get_object_or_404
from django.template.context_processors import request
from django.views import View

from accounts.forms import UserLoginForm
from accounts.models import User


class UserRegisterView(View):
    def get(self, request):
        return render(request, "accounts/register.html")


class UserLoginView(View):
    template_name = "accounts/login.html"
    form_class = UserLoginForm

    def get(self, request):
        return render(request, self.template_name, {"form": self.form_class()})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            pass
        return render(request, self.template_name, {"form": form})


class UserProfileView(View):
    def get(self, request, **kwargs):
        profile_user = request.user if request.user.pk == kwargs['user_id'] else  get_object_or_404(User, pk=kwargs['user_id'])
        return render(request, "accounts/profile.html", {'user': profile_user})
