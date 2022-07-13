from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):

    user_from_model=models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    is_retired=models.BooleanField(default=True)
    previous_companies=models.TextField()
    location=models.CharField(max_length=100)
    photo_url=models.TextField()


    def __str__(self):
        return str(self.user_from_model)

class Post(models.Model):
    username=models.ForeignKey(Profile, on_delete=models.CASCADE, default='User Name')
    name_of_user=models.CharField(max_length=50)
    title=models.CharField(max_length=150)
    post_content=models.TextField()
    post_date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name_of_user

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=50)
    content=models.TextField()
    created_date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.author

        