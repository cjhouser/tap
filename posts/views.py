from django.shortcuts import render

from .models import Post

def index(request):
    posts = Post.objects.order_by('-creation_date')
    context = {
        'posts': posts
    }
    return render(request, 'posts/index.html', context)