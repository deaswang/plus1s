from django.contrib import admin

from .models import Thread, Post, Comment

admin.site.register(Thread)
admin.site.register(Post)
admin.site.register(Comment)