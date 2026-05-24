from django.shortcuts import render
from django.views import View


class HomeView(View):
    def get(self, request):
        return render(request, "post/home.html")


class ExploreView(View):
    def get(self, request):
        return render(request, "post/explore.html")


class PostCreateView(View):
    def get(self, request):
        return render(request, "post/create.html")
