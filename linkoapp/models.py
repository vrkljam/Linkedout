from tkinter import CASCADE
from django.db import models

# Create your models here.

class Post(models.Model):
    author=models.CharField(max_length=40)
    title=models.CharField(max_length=150)
    post_content=models.TextField()
    post_date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.author

class Comments(models.Model):
    post = models.ForeignKey(Post, on_delete=CASCADE)
    author = models.CharField(max_length=50)
    content=models.TextField()
    created_date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.author

        