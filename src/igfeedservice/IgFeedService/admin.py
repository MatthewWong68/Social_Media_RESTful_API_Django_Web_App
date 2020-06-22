from django.contrib import admin

from .models import Page, Post, Hashtag

# Register your models here.

admin.site.register(Page)
admin.site.register(Post)
admin.site.register(Hashtag)