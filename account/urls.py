from django.urls import path
from . import views


app_name = "account"
urlpatterns = [
    path("profile/<int:user_id>/", views.UserProfileView.as_view(), name="user_profile")
]

