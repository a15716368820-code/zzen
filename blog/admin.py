from django.contrib import admin
from .models import Post, Category, SiteSetting


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "status", "published_at", "created_at")
    list_filter = ("status", "category", "created_at")
    search_fields = ("title", "summary", "content")
    prepopulated_fields = {"slug": ("title",)}
    autocomplete_fields = ("author",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


@admin.register(SiteSetting)
class SiteSettingAdmin(admin.ModelAdmin):
    list_display = ("site_title", "author_name", "theme", "allow_comments")
