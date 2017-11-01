from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils import timezone

from .forms import PostCreateForm
from .models import Post

User = get_user_model()


def post_list(request):
    posts = Post.objects.order_by('-created_date')
    # posts = Post.objects.filter(published_date__lte=timezone.now())
    context = {
        'title': 'Django from djangogirls',
        'posts': posts,
    }
    return render(request, 'blog/post_list.html', context=context)


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    context = {
        'post': post,
    }
    return render(request, 'blog/post_detail.html', context=context)


def post_create(request):
    if request.method == 'GET':
        form = PostCreateForm()
        context = {
            'form': form,
        }
        return render(request, 'blog/post_create.html', context=context)
    elif request.method == 'POST':
        form = PostCreateForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            text = form.cleaned_data['text']
            user = User.objects.first()
            post = Post.objects.create(
                author=user,
                title=title,
                text=text
            )
            return redirect('post_detail', pk=post.pk)
        else:
            context = {
                'form':form,
            }
            return render(request, 'blog/post_create.html', context=context)