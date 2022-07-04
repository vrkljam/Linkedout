from django.db import models

# Create your models here.

class Post(models.Model):
    author=models.CharField(max_length=40)
    title=models.CharField(max_length=150)
    post_content=models.TextField()
    post_date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.author