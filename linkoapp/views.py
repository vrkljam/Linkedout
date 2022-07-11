from django.shortcuts import render, redirect

# Create your views here.
from .models import Post, Comment, Profile
from .forms import PostForm, CommentForm, ProfileForm,TestForm
from django.views import View
# from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
# Functional based methods 

class Home(TemplateView):
    template_name = "linkoapp/home.html"


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

# def profile_view(request):
#     profile_form=ProfileForm()
@login_required 
def post_create(request):
    if request.method=='POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('post_detail', pk=post.pk )
    else:
        form = PostForm()
    return render(request, 'linkoapp/post_form.html', {'form':form})

@login_required
def comment_create(request):
    if request.method=='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            comment = form.save()
            return redirect('comment_detail', pk=comment.pk )
    else:
        form = CommentForm()
    return render(request, 'linkoapp/comment_form.html', {'form':form})

@login_required
def post_edit(request,pk):
    post=Post.objects.get(pk=pk)
    if request.method=='POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post=form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'linkoapp/post_edit_form.html', {'form':form})

@login_required
def post_redit(request,pk):
    post=Post.objects.get(pk=pk)
    if request.method=='POST':
        form = TestForm(request.POST, instance=post)
        if form.is_valid():
            post=form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = TestForm(instance=post)
    return render(request, 'linkoapp/post_redit_form.html', {'form':form})

@login_required
def comment_edit(request,pk):
    post=Comment.objects.get(pk=pk)
    if request.method=='POST':
        form = CommentForm(request.POST, instance=post)
        if form.is_valid():
            comment=form.save()
            return redirect('comment_detail', pk=post.pk)
    else:
        form = CommentForm(instance=post)
    return render(request, 'linkoapp/comment_form.html', {'form':form})

@login_required
def post_delete(request,pk):
    Post.objects.get(id=pk).delete()
    return redirect('post_list')

@login_required
def comment_delete(request,pk):
    Comment.objects.get(id=pk).delete()
    return redirect('comment_list')



# class based methods 

# class ProfileList(ListView):
#     template_name = 'post_list.html'

#     def get_context_data(self, **kwargs):
#         context=super().get_context_data(**kwargs)
#         context['profile']=Profile.objects.all()
#         return context

# class PostList(ListView):
#     template_name = 'post_list.html'

#     def get_context_data(self, **kwargs):
#         context=super().get_context_data(**kwargs)
#         context['posts']=Post.objects.all()
#         return context

# class CommentList(ListView):
#     template_name = 'comment_list.html'

#     def get_context_data(self, **kwargs):
#         context=super().get_context_data(**kwargs)
#         context['comments']=Comment.objects.all()
#         return context
        
# class PostCreate(CreateView):
#     model= Post
#     fields=['name_of_user','title','post_content']
#     template_name= 'linkoapp/post_form.html'
#     success_url='/'

# class CommentCreate(CreateView):
#     model= Comment
#     fields=['post','author','content',]
#     template_name= 'linkoapp/comment_form.html'
#     success_url='/comments/'

# class PostEdit(UpdateView):
#     model= Post
#     fields=['name_of_user','title','post_content']
#     template_name= 'linkoapp/post_edit_form.html'
#     success_url='/'

# class CommentEdit(UpdateView):
#     model= Comment
#     fields=['post','author','content',]
#     template_name= 'linkoapp/comment_edit_form.html'
#     success_url='/comments/'

# class PostDelete(DeleteView):
#     model: Post
#     template_name= 'linkoapp/post_delete_form.html'
#     success_url='/'

# class CommentDelete(DeleteView):
#     model: Comment
#     template_name= 'linkoapp/comment_delete_form.html'
#     success_url='/comments/'


# def comment_list(request):
#     comments = Comment.objects.all()
#     return render(request,'linkoapp/comment_list.html', {'comments':comments})

# def post_detail(request, pk):
#     post=Post.objects.get(id=pk)
#     return render(request, 'linkoapp/post_detail.html', {'post':post})

# def comment_detail(request,pk):
#     comment=Comment.objects.get(id=pk)
#     return render(request, 'linkoapp/comment_detail.html', {'comment':comment})
