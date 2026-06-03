from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

from blog.forms import BlogCreateForm
from blog.models import Blog


class HomeView(View):
    def get(self, request):
        blogs = (
            Blog.objects.filter(status=Blog.BlogStatus.VERIFIED)
            .select_related("author")
            .only("cover", "title", "preview_body", "slug", "author__username", "author__id")
            )
        paginator = Paginator(blogs, 10)
        page_obj = paginator.get_page(request.GET.get("page"))
        return render(request, "blog/home.html", {"page_obj": page_obj})


class ExploreView(View):
    def get(self, request):
        return render(request, "blog/explore.html")


class BlogCreateView(LoginRequiredMixin, View):
    form_class = BlogCreateForm
    template_name = "blog/create.html"

    def get(self, request):
        return render(request, self.template_name, {"form": self.form_class()})

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            messages.success(request, "بلاگ شما با موفقیت ثبت شد و پس از تایید نمایش داده میشود.")
            return redirect("blog:home")
        return render(request, self.template_name, {"form": form})
    

class BlogDetailView(View):
    def get(self, request, blog_id, blog_slug):
        only_fields = ["title", "body", "cover", "created_at", "author__id", "author__username"]
        if request.user.is_superuser:
            only_fields.append("status")
        blog = get_object_or_404(
            Blog.objects.select_related("author").only(*only_fields),
            pk=blog_id,
            slug=blog_slug
        )
        return render(request, "blog/detail.html", {"blog": blog})
