"""personal_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blog import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('chess/', views.chess, name='chess'),
    path('chess/<int:pk>/', views.chess_post_detail, name='chess_post_detail'),
    path('news/', views.news, name='news'),
    path('news/<int:pk>/', views.news_post_detail, name='news_post_detail'),
    path('lib/', views.lib, name='lib'),
    path('lib/<int:pk>/', views.lib_post_detail, name='lib_post_detail'),
    path('media/', views.media, name='media'),
    path('media/<int:pk>/', views.media_post_detail, name='media_post_detail'),
    path('guest/', views.guest, name='guest'),
    path('guest/<int:pk>/', views.guest_post_detail, name='guest_post_detail,'),
] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

