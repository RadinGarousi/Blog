from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group


admin.site.unregister(Group)

User = get_user_model()
@admin.register(User)
class CustomUserAdmin(UserAdmin):

    readonly_fields = ["last_login", "date_joined", "last_update"]

    fieldsets = [
        *(item for item in UserAdmin.fieldsets if item[0] != "Permissions" and item[0] != "Important dates"),
        ("Important dates", {"fields": ("last_login", "date_joined", "last_update")}),
        ("profile", {"fields": ("bio", "is_private", "account_status", "country", "city", "avatar", "poster")})
    ]

    add_fieldsets = [
        (None, {"fields": ("username", "email", "password1", "password2")})
    ]
