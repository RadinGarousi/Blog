import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.templatetags.static import static
from django.urls import reverse

from .validators import validate_avatar, validate_poster


def user_avatar_path(instance, filename):
    return f"{instance.pk}/avatar_{uuid.uuid4()}.{filename.split('.')[-1]}"


def user_poster_path(instance, filename):
    return f"{instance.pk}/poster_{uuid.uuid4()}.{filename.split('.')[-1]}"


class User(AbstractUser):
    class AccountStatus(models.TextChoices):
        PENDING = "P", "Pending"
        REJECTED = "R", "Rejected"
        VERIFIED = "V", "Verified"

    email = models.EmailField(unique=True)
    avatar = models.ImageField(upload_to=user_avatar_path, blank=True, null=True, validators=[validate_avatar])
    poster = models.ImageField(upload_to=user_poster_path, blank=True, null=True, validators=[validate_poster])
    country = models.CharField(max_length=50, blank=True, default="")
    city = models.CharField(max_length=50, blank=True, default="")
    bio = models.CharField(max_length=300, blank=True, default="")
    is_private = models.BooleanField(default=False)
    # This field for reporting system . report system for next versions
    account_status = models.CharField(max_length=1, default=AccountStatus.VERIFIED, choices=AccountStatus)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-date_joined", "username"]

    # avatar_url and poster_url methods:
    # To avoid hard coding image paths in templates and to provide a default image
    # when the user has not uploaded an avatar or poster.
    # Default images are served from the static files directory.
    def get_avatar_url(self):
        return self.avatar.url if self.avatar else static("images/default/avatar.webp")

    def get_poster_url(self):
        return self.poster.url if self.poster else static("images/default/poster.webp")

    def get_absolute_url(self):
        return reverse("accounts:user_profile", kwargs={"user_id": self.pk})

    def save(self, *args, **kwargs):

        if self.account_status == self.AccountStatus.VERIFIED and self.is_active == False:
            self.is_active = True
        elif self.account_status in [self.AccountStatus.REJECTED, self.AccountStatus.PENDING] and self.is_active == True:
            self.is_active = False
        return super().save(*args, **kwargs)
