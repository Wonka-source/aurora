from django.shortcuts import render, get_object_or_404
from django.contrib.auth import PermissionDenied

from .models import Post


def post_list(request):
    """
    A view that displays a list of published blog posts.
    """
    posts = Post.objects.filter(status=1)
    context = {
        'posts': posts
    }

    return render(request, 'post_list.html', context)


def post_detail(request, post_id):
    """
    A view that displays the detail of a blog post,
    """
    post = get_object_or_404(Post, id=post_id)
    template = "post_detail.html"
    context = {
        "page_title": "Post Detail",
        "post": post,
    }
    if post.status == 1:
        return render(request, template, context)
    elif (post.status == 0 or post.status == 2) and request.user.is_superuser:
        return render(request, template, context)
    else:
        raise PermissionDenied
