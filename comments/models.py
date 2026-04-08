from django.db import models
from django.contrib.auth import get_user_model
from blog.models import Post

User = get_user_model()


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    nickname = models.CharField(max_length=50)
    email = models.EmailField(blank=True)
    content = models.TextField()
    is_approved = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "评论"
        verbose_name_plural = "评论"

    def __str__(self):
        return f"{self.nickname}: {self.content[:20]}"
