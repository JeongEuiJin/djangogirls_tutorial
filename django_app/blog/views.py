from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone

from blog.models import Post


def post_list(request):
    # posts = Post.objects.all()
    posts = Post.objects.filter(published_date__lte=timezone.now())
    context = {
        'title': 'Django from djangogirls',
        'posts': posts,
    }
    return render(request, 'blog/post_list.html', context=context)
