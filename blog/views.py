from django.shortcuts import render
from .models import Post
from django.contrib.auth.decorators import login_required
from django.contrib.auth import PermissionDenied
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User


def post_list(request):
    posts = Post.objects.filter(status=1)
    context = {
        'posts': posts
    }

    return render(request, 'post_list.html', context)


def post_detail(request, post_id):
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
