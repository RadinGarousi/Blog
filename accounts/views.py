from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from accounts.forms import UserLoginForm

User = get_user_model()


class UserRegisterView(View):
    def get(self, request):
        return render(request, "accounts/register.html")


class UserLoginView(View):
    template_name = "accounts/login.html"
    form_class = UserLoginForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("post:home")
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, self.template_name, {"form": self.form_class()})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['login'], password=cd['password'])
            if user:
                login(request, user)
                messages.success(request, "شما با موفقیت وارد شدید")
                next_url = request.GET.get("next", None)
                if next_url:
                    return redirect(next_url)
                else:
                    return redirect(user)
        form.add_error(None, "اطلاعات وارد شده نادرست است.")
        return render(request, self.template_name, {"form": form})


class UserProfileView(View):
    def get(self, request, **kwargs):
        profile_user = request.user if request.user.pk == kwargs['user_id'] else get_object_or_404(User,
                                                                                                   pk=kwargs['user_id'])
        return render(request, "accounts/profile.html", {'user': profile_user})
