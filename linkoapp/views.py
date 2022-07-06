from django.shortcuts import render

# Create your views here.
from .models import Post, Comment


def post_list(request):
    posts = Post.objects.all() 
    return render (request, 'linkoapp/post_list.html', {'posts':posts})

def comment_list(request):
    comments = Comment.objects.all()
    return render(request,'linkoapp/comment_list.html', {'comments':comments})