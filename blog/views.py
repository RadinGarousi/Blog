from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import View

from blog.models import Blog


class HomeView(View):
    def get(self, request):
        blogs = Blog.objects.filter(status=Blog.BlogStatus.VERIFIED).only("title", "preview_body", "author__username").select_related("author")
        paginator = Paginator(blogs, 10)
        page_obj = paginator.get_page(request.GET.get("page"))
        return render(request, "blog/home.html", {"blogs": page_obj})


class ExploreView(View):
    def get(self, request):
        return render(request, "blog/explore.html")


class PostCreateView(View):
    def get(self, request):
        return render(request, "blog/create.html")
