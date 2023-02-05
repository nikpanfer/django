from django.contrib import admin

from authapp import models as mainapp_models


@admin.register(mainapp_models.CustomUser)
class NewsAdmin(admin.ModelAdmin):
    search_fields = ["username", "first_name", "last_name", "email"]
    list_display = [
        "id",
        "username",
        "first_name",
        "last_name",
        "age",
        "email",
        "is_superuser",
        "is_staff",
        "is_active",
        "last_login",
        "date_joined",
    ]
    ordering = ["-is_superuser", "-is_staff", "-is_active", "username"]
    list_per_page = 15
    list_filter = ["is_superuser", "is_staff", "is_active"]
