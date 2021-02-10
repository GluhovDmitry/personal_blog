from django.contrib import admin
from blog.models import Chess_post
from blog.models import News_post
from blog.models import Lib_post
from blog.models import Media_post
from blog.models import Guest_post

admin.site.register(Chess_post)
admin.site.register(News_post)
admin.site.register(Lib_post)
admin.site.register(Media_post)
admin.site.register(Guest_post)
