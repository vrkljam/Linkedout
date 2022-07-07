from django.shortcuts import render, redirect

# Create your views here.
from .models import Post, Comment
from .forms import PostForm, CommentForm

# Functional based methods 
def post_list(request):
    posts = Post.objects.all() 
    return render (request, 'linkoapp/post_list.html', {'posts':posts})

def comment_list(request):
    comments = Comment.objects.all()
    return render(request,'linkoapp/comment_list.html', {'comments':comments})

def post_detail(request, pk):
    post=Post.objects.get(id=pk)
    return render(request, 'linkoapp/post_detail.html', {'post':post})

def comment_detail(request,pk):
    comment=Comment.objects.get(id=pk)
    return render(request, 'linkoapp/comment_detail.html', {'comment':comment})

def post_create(request):
    if request.method=='POST':
        form=PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('post_detail', pk=post.pk )
        else:
            form = PostForm()
        return render(request, 'linkoapp/post_form.html', {'form':form})

def comment_create(request):
    if request.method=='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            comment = form.save()
            return redirect('comment_detail', pk=comment.pk )
        else:
            form = CommentForm()
        return render(request, 'linkoapp/comment_form.html', {'form':form})
        

