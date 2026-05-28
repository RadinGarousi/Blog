from django.urls import path

from . import views

app_name = "blog"
urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("explore/", views.ExploreView.as_view(), name="explore"),
    path("blog/create/", views.PostCreateView.as_view(), name="post_create")
]
