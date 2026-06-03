import uuid
from pathlib import Path

from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
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
    title = models.CharField(max_length=70)
    body = models.TextField()
    slug = models.SlugField(allow_unicode=True)
    cover = models.ImageField(unique=True, upload_to=blog_cover_path, verbose_name="Blog Image")
    preview_body = models.CharField(max_length=403, editable=False)
    status = models.CharField(max_length=1, choices=BlogStatus, default=BlogStatus.PENDING)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at", "title"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:blog_detail", kwargs={"blog_id": self.pk, "blog_slug": self.slug})

    def save(self,*args, **kwargs):
        body_sliced = " . ".join(item for item in self.body[:300].splitlines() if item)
        self.preview_body = body_sliced + "..." if len(self.body) > 300 else body_sliced
        if self.pk is None and not self.slug:
            self.slug = slugify(self.title[:50], allow_unicode=True)
        super().save(*args, **kwargs)


class BlogVote(models.Model):
    class VoteStatus(models.TextChoices):
        LIKE = "L", "Like"
        DISLIKE = "D", "Dislike"

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="votes", verbose_name="User")
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="votes")
    status = models.CharField(max_length=1, choices=VoteStatus)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-updated_at"]

    def __str__(self):
        return f"{self.author} **{self.status}** {self.blog}"
