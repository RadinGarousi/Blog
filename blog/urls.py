from django.urls import path

from . import views

app_name = "blog"
urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("explore/", views.ExploreView.as_view(), name="explore"),
    path("blog/create/", views.BlogCreateView.as_view(), name="blog_create"),
    path("blog/<int:blog_id>/<slug:blog_slug>/detail/", views.BlogDetailView.as_view(), name="blog_detail"),
    path("blog/<int:blog_id>/like/", views.BlogLikeView.as_view(), name="blog_like"),
    path("blog/dislike/<int:blog_id>/", views.BlogDislikeView.as_view(), name="blog_dislike"),
    path("blog/<int:blog_id>/comment/create/", views.CommentCreateView.as_view(), name="comment_create")
]
