from django.shortcuts import render, get_object_or_404
from django.views import View

from account.models import User


class UserProfileView(View):
    def get(self, request, **kwargs):
        user = get_object_or_404(User, pk=kwargs['user_id'])
        return render(request, "account/profile.html", {'user': user})
