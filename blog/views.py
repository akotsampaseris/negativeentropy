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
    try:
        cat = PostCategory.objects.get_object_or_404(slug=slug)
        posts = Post.objects.filter(category=cat)
    except:
        cat = []
        posts = []

    context = {
        "cat": cat,
        "posts": posts
    }

    return render(request, 'blog/category.html', context)


def post(request, slug):
    post = Post.objects.get_object_or_404(slug=slug)

    context = {
        "post": post
    }

    return render(request, 'blog/post.html', context)
