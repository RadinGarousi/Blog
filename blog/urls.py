from django.urls import path

from . import views

app_name = "blog"
urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("explore/", views.ExploreView.as_view(), name="explore"),
    path("blog/create/", views.BlogCreateView.as_view(), name="blog_create"),
    path("blog/detail/<int:blog_id>/<slug:blog_slug>/", views.BlogDetailView.as_view(), name="blog_detail")
]
