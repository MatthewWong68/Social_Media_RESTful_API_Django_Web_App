from django.contrib import admin

# Register your models here.
from .models import Feed
# from .models import Feed, FbUser


admin.site.register(Feed)
# admin.site.register(FbUser)
