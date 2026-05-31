from django.contrib import admin

from blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    readonly_fields = ["created_at", "updated_at"]
    raw_id_fields = ["author"]
    empty_value_display = "This field is readonly . After save blog you can see data"
    prepopulated_fields = {"slug": ["title"]}
