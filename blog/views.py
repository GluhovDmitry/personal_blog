from django.shortcuts import render, get_object_or_404
from .models import Chess_post, News_post, Lib_post, Media_post, Guest_post


def home(request):
        return render(request, 'home.html', {})


def chess(request):
        posts = Chess_post.objects.all()
        return render(request, 'chess.html', {'posts': posts})


def news(request):
        posts = News_post.objects.all()
        return render(request, 'news.html', {'posts': posts})


def lib(request):
        posts = Lib_post.objects.all()
        return render(request, 'lib.html', {'posts': posts})


def media(request):
        posts = Media_post.objects.all()
        return render(request, 'media.html', {'posts': posts})


def guest(request):
        posts = Guest_post.objects.all()
        return render(request, 'guest.html', {'posts': posts})


def chess_post_detail(request, pk):
        post = get_object_or_404(Chess_post, pk=pk)
        return render(request, 'post.html', {'post': post})


def news_post_detail(request, pk):
        post = get_object_or_404(News_post, pk=pk)
        return render(request, 'post.html', {'post' : post})


def lib_post_detail(request, pk):
        post = get_object_or_404(Lib_post, pk=pk)
        return render(request, 'post.html', {'post' : post})


def media_post_detail(request, pk):
        post = get_object_or_404(Media_post, pk=pk)
        return render(request, 'post.html', {'post' : post})


def guest_post_detail(request, pk):
        post = get_object_or_404(Guest_post, pk=pk)
        return render(request, 'post.html', {'post' : post})