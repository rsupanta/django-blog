from django.shortcuts import render
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all().filter().order_by('-date_posted')
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', context={})
