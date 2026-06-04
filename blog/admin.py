from django.contrib import admin

from blog.models import Blog, BlogVote, BlogComment


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    readonly_fields = ["created_at", "updated_at"]
    raw_id_fields = ["author"]
    empty_value_display = "This field is readonly . After save blog you can see data"
    prepopulated_fields = {"slug": ["title"]}
    list_display = ["title", "author", "status", "created_at", "updated_at"]
    list_filter = ["author", "status", "created_at", "updated_at"]


@admin.register(BlogVote)
class BlogVoteAdmin(admin.ModelAdmin):
    readonly_fields = ["created_at", "updated_at"]
    empty_value_display = "This field is readonly . After save blog you can see data"
    raw_id_fields = ["author", "blog"]
    list_display = ["type", "blog", "author", "created_at", "updated_at"]
    list_filter = ["author", "blog", "type", "created_at", "updated_at"]


@admin.register(BlogComment)
class BlogCommentAdmin(admin.ModelAdmin):
    raw_id_fields = ["author", "blog", "parent"]
    readonly_fields = ["created_at"]
    empty_value_display = "This field is readonly . After save blog you can see data"
    list_display = ["created_at", "author", "blog", "status"]
    list_filter = ["author", "status", "blog", "created_at"]


