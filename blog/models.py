from django.db import models
from django.contrib.auth import get_user_model
from taggit.managers import TaggableManager
from markdown import markdown
from django.utils import timezone
import bleach

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True)

    class Meta:
        verbose_name = "分类"
        verbose_name_plural = "分类"

    def __str__(self):
        return self.name


class Post(models.Model):
    STATUS_CHOICES = (
        ("draft", "草稿"),
        ("published", "已发布"),
    )

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name="posts")
    summary = models.TextField(blank=True)
    content = models.TextField()
    content_html = models.TextField(blank=True, editable=False)
    tags = TaggableManager(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="draft")
    is_featured = models.BooleanField(default=False)
    view_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ["-published_at", "-created_at"]
        verbose_name = "文章"
        verbose_name_plural = "文章"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        html = markdown(self.content)
        self.content_html = bleach.clean(
            html,
            tags=["p", "h1", "h2", "h3", "strong", "em", "ul", "ol", "li", "code", "pre", "blockquote", "img"],
            attributes={"img": ["src", "alt"]},
        )

        if self.status == "published" and not self.published_at:
            self.published_at = timezone.now()

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("post_detail", kwargs={"slug": self.slug})


class SiteSetting(models.Model):
    THEME_CHOICES = (
        ("cards", "卡片"),
        ("minimal", "极简"),
        ("dark", "暗黑"),
    )

    site_title = models.CharField(max_length=100, default="个人博客")
    author_name = models.CharField(max_length=100, default="Zzen")
    theme = models.CharField(max_length=20, choices=THEME_CHOICES, default="cards")
    allow_comments = models.BooleanField(default=True)

    class Meta:
        verbose_name = "站点设置"
        verbose_name_plural = "站点设置"

    def __str__(self):
        return "站点设置"
