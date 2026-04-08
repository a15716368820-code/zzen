from django.contrib.auth import get_user_model
from blog.models import Category, Post, SiteSetting
from django.utils import timezone

User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin12345')

setting, _ = SiteSetting.objects.get_or_create(id=1)
setting.site_title = '个人博客'
setting.author_name = 'Zzen'
setting.theme = 'cards'
setting.allow_comments = True
setting.save()

cat, _ = Category.objects.get_or_create(name='默认分类', slug='default')

if not Post.objects.filter(slug='hello-world').exists():
    Post.objects.create(
        title='第一篇文章',
        slug='hello-world',
        author=User.objects.first(),
        category=cat,
        summary='欢迎使用你的个人博客。',
        content='这是第一篇文章，支持 **Markdown**。',
        status='published',
        published_at=timezone.now(),
    )
