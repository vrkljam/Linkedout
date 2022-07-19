from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Portrait(models.Model):

    user=models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='profile')
    location=models.CharField(max_length=100)
    first_name=models.CharField(max_length=50,null=True)
    last_name=models.CharField(max_length=50,null=True)
    email=models.EmailField(max_length=200, null=True)
    previous_companies=models.CharField(max_length=300, null=True)
    photo_url=models.TextField(null=True)

    def __str__(self):
        return self.last_name

class Post(models.Model):
    username=models.ForeignKey(Portrait, on_delete=models.CASCADE, related_name='portrait')
    title=models.CharField(max_length=150)
    post_content=models.TextField()
    post_date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='tacos')
    author = models.CharField(max_length=50)
    content=models.TextField()
    created_date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.author

class Buckets(models.Model):
    userB=models.ForeignKey(Portrait, on_delete=models.CASCADE, null=True, related_name='items')
    title=models.CharField(max_length=200)
    complete=models.BooleanField(default=False)
    created_date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

        