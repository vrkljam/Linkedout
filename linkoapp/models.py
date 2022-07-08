from django.db import models

# Create your models here.

# can i use the username from the sign-in/create account?

# class Profile(models.Model):
#     username=models.foreignKey(User, on.....)---would like this from the login
      first_name
      last_name  
#     is_retired=models.BooleanField(default=True)
#     previous_companies=models.TextField()
    # email=models.EmailField()
    # location=models.CharField(max_length=100)
    # photo_url=models.TextField()


#     def __str__(self):
#         return self.username

class Post(models.Model):
    # username=models.ForeignKey(Profile, on_delete=models.CASCADE)
    name_of_user=models.CharField(max_length=50, default='')
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

        