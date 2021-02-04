from django.shortcuts import render

# Create your views here.
def home(request):
        return render(request, 'home.html', {})
def chess(request):
        return render(request, 'chess.html', {})
def news(request):
        return render(request, 'news.html', {})
def lib(request):
        return render(request, 'lib.html', {})
def media(request):
        return render(request, 'media.html', {})
def guest(request):
        return render(request, 'guest.html', {})