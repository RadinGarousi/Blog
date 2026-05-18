import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models

from .validators import validate_avatar, validate_poster


def user_avatar_path(instance, filename):
    return f"{instance.username}/avatar_{uuid.uuid4()}.{filename.split('.')[-1]}"

def user_poster_path(instance, filename):
    return f"{instance.username}/poster_{uuid.uuid4()}.{filename.split('.')[-1]}"    

class User(AbstractUser):

    class ProfileStatus(models.TextChoices):
        PENDING = "P", "Pending"
        REJECTED = "R", "Rejected"
        VERIFIED = "V", "Verified"
    
    email = models.EmailField(unique=True)
    avatar = models.ImageField(upload_to=user_avatar_path, blank=True, null=True, validators=[validate_avatar])
    poster = models.ImageField(upload_to=user_poster_path, blank=True, null=True, validators=[validate_poster])
    country = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    bio = models.CharField(max_length=300, blank=True, null=True)
    is_private = models.BooleanField(default=False)
    profile_status = models.CharField(max_length=1, default=ProfileStatus.VERIFIED, choices=ProfileStatus.choices) # This field for reporting system . report system for next versions
    updated_at = models.DateTimeField(auto_now=True)
