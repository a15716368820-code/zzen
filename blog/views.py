from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.views.generic import ListView, DetailView
from django.contrib import messages

from .models import Post, Category, SiteSetting
from .forms import CommentForm


def get_site_setting():
    setting = SiteSetting.objects.first()
    if not setting:
        setting = SiteSetting.objects.create()
    return setting


class PostListView(ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "posts"
    paginate_by = 8

    def get_queryset(self):
        qs = Post.objects.filter(status="published")
        q = self.request.GET.get("q")
        tag = self.request.GET.get("tag")
        category = self.request.GET.get("category")
        if q:
            qs = qs.filter(Q(title__icontains=q) | Q(summary__icontains=q) | Q(content__icontains=q))
        if tag:
            qs = qs.filter(tags__name=tag)
        if category:
            qs = qs.filter(category__slug=category)
        return qs.select_related("author", "category").prefetch_related("tags")

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["categories"] = Category.objects.all()
        ctx["site"] = get_site_setting()
        ctx["latest_posts"] = Post.objects.filter(status="published").order_by("-published_at")[:5]
        return ctx


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/detail.html"
    context_object_name = "post"

    def get_queryset(self):
        return Post.objects.filter(status="published").select_related("author", "category").prefetch_related("tags")

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["site"] = get_site_setting()
        ctx["comment_form"] = CommentForm()
        return ctx

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object
            comment.save()
            messages.success(request, "评论已提交")
            return redirect(self.object.get_absolute_url())
        ctx = self.get_context_data()
        ctx["comment_form"] = form
        return render(request, self.template_name, ctx)


def rss_feed(request):
    from django.contrib.syndication.views import Feed

    class LatestPostsFeed(Feed):
        title = "个人博客"
        link = "/"
        description = "个人博客 RSS"

        def items(self):
            return Post.objects.filter(status="published").order_by("-published_at")[:20]

        def item_title(self, item):
            return item.title

        def item_description(self, item):
            return item.summary or item.content[:200]

    return LatestPostsFeed()(request)
