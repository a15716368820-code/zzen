from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from blog.models import Post


class PostPerformanceTests(TestCase):
    def test_published_post_can_be_created(self):
        user = get_user_model().objects.create_user(
            username="tester",
            password="testpass123",
        )

        post = Post.objects.create(
            title="Test Post",
            slug="test-post",
            author=user,
            content="# Hello",
            status="published",
        )

        self.assertIsNotNone(post.published_at)
        self.assertTrue(post.content_html)
