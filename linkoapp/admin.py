from django.contrib import admin

# Register your models here.
from .models import BucketList, Post,Comment, Portrait

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Portrait)
admin.site.register(BucketList)
