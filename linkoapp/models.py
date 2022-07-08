from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):

    testing=models.ForeignKey(User, on_delete=models.CASCADE)
    is_retired=models.BooleanField(default=True)
    previous_companies=models.TextField()
    location=models.CharField(max_length=100)
    photo_url=models.TextField()


    def __str__(self):
        return self.testing

class Post(models.Model):
    # username=models.ForeignKey(Profile, on_delete=models.CASCADE, default='1')
    name_of_user=models.CharField(max_length=50, default='1')
    title=models.CharField(max_length=150)
    post_content=models.TextField()
    post_date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name_of_user

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.CharField(max_length=50)
    content=models.TextField()
    created_date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.author

        