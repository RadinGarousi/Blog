import uuid
from pathlib import Path

from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify

User = get_user_model()


def blog_cover_path(instance, filename):
    return f"user_{instance.author_id}/blogs/blog_{instance.blog_uuid}/cover_{uuid.uuid4()}{Path(filename).suffix}"

class Blog(models.Model):
    class BlogStatus(models.TextChoices):
        VERIFIED ="V", "Verified"
        PENDING = "P", "Pending"
        REJECTED = "R", "Rejected"

    blog_uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=90)
    body = models.TextField()
    slug = models.SlugField()
    cover = models.ImageField(unique=True, upload_to=blog_cover_path, verbose_name="Blog Image")
    preview_body = models.CharField(max_length=400, editable=False)
    status = models.CharField(max_length=1, choices=BlogStatus, default=BlogStatus.PENDING)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at", "title"]

    def __str__(self):
        return self.title

    def save(self,*args, **kwargs):
        self.preview_body = self.body[:400]
        if self.pk is None and not self.slug:
            self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)

