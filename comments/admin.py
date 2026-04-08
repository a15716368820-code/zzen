from django.contrib import admin
from .models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("post", "nickname", "is_approved", "created_at")
    list_filter = ("is_approved", "created_at")
    search_fields = ("nickname", "content")
    autocomplete_fields = ("post",)
