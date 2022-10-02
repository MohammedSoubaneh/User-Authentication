from django.shortcuts import render
from .models import Post

def get_posts(self):
    posts = Post.objects.all()
    return render({
        'post': posts
    })