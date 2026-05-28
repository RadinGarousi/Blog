from django.shortcuts import render
from django.views import View


class HomeView(View):
    def get(self, request):
        return render(request, "blog/home.html")


class ExploreView(View):
    def get(self, request):
        return render(request, "blog/explore.html")


class PostCreateView(View):
    def get(self, request):
        return render(request, "blog/create.html")
