from django.shortcuts import render, redirect, get_object_or_404

from .models import Post, PostCategory

# Create your views here.
def index(request):
    cats  = PostCategory.objects.all()
    posts = Post.objects.all()

    context = {
        "cats": cats,
        "posts": posts
    }

    return render(request, 'blog/index.html', context)


def category(request, slug):
    cat = get_object_or_404(PostCategory, slug=slug)
    posts = Post.objects.filter(category=cat)

    context = {
        "cat": cat,
        "posts": posts
    }

    return render(request, 'blog/category.html', context)


def post(request, slug):
    post = get_object_or_404(Post, slug=slug)

    context = {
        "post": post
    }

    return render(request, 'blog/post.html', context)
