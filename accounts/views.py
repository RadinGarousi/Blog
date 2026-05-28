from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from accounts.forms import UserLoginForm, UserRegisterForm

User = get_user_model()


class UserRegisterView(View):
    template_name = "accounts/register.html"
    form_class = UserRegisterForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.warning(request, "شما قبلا وارد شده اید")
            return redirect("blog:home")
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, self.template_name, {"form": self.form_class()})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend="django.contrib.auth.backends.ModelBackend")
            messages.success(request, "حساب شما با موفقیت ساخته شد و وارد شدید")
            return redirect(user.get_absolute_url())
        return render(request, self.template_name, {"form": form})


class UserLoginView(View):
    template_name = "accounts/login.html"
    form_class = UserLoginForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.warning(request, "شما قبلا وارد شده اید.")
            return redirect("blog:home")
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
                    return redirect(user.get_absolute_url())
        form.add_error(None, "اطلاعات وارد شده نادرست است.")
        return render(request, self.template_name, {"form": form})


class UserLogoutView(View):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.warning(request, "شما وارد نشده اید که خارج شوید")
            return redirect("blog:home")
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        logout(request)
        messages.success(request, "شما با موفقیت خارج شدید.")
        return redirect("blog:home")


class UserProfileView(View):
    def get(self, request, **kwargs):
        if request.user.pk == kwargs['user_id']:
            profile_user = request.user
        else:
            profile_user = get_object_or_404(User, pk=kwargs['user_id'])
        return render(request, "accounts/profile.html", {'user': profile_user})
