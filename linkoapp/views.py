from django.shortcuts import render, redirect

# Create your views here.
from .models import Post, Comment, Portrait
from .forms import PostForm, CommentForm,TestForm, PortraitForm
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
# Functional based methods 

class Home(TemplateView):
    template_name = "linkoapp/home.html"

# -----Read All part of Crud--------
class PostList(TemplateView):
    template_name = 'linkoapp/post_list.html'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['posts']=Post.objects.all()
        return context

class CommentList(TemplateView):
    template_name = 'linkoapp/comment_list.html'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['comments']=Comment.objects.all()
        return context

class PortraitList(TemplateView):
    template_name = 'linkoapp/portrait_page.html'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['portraits']=Portrait.objects.all()
        return context

    

# --------View one item----------
class PostDetail(DetailView):
    model=Post
    template_name='linkoapp/post_detail.html'

class CommentDetail(DetailView):
    model=Comment
    template_name='linkoapp/comment_detail.html'

class PortraitDetail(DetailView):
    model=Portrait
    template_name='linkoapp/portrait_detail.html'

# ---Create views---------
class PostCreate(CreateView):
    model= Post
    fields=['username','title','post_content']
    template_name= 'linkoapp/post_form.html'
    success_url='/'

class CommentCreate(CreateView):
    model= Comment
    fields=['post','author','content',]
    template_name= 'linkoapp/comment_form.html'
    success_url='/comments/'

class PortraitCreate(CreateView):
    model= Portrait
    fields=['location','first_name','last_name','email','photo_url',]
    template_name= 'linkoapp/portrait_form.html'
    success_url='/'

# ------Update Views--------
class PostEdit(UpdateView):
    model= Post
    fields=['name_of_user','title','post_content']
    template_name= 'linkoapp/post_edit_form.html'
    success_url='/'

# @login_required
# def post_redit(request,pk):
#     post=Post.objects.get(pk=pk)
#     if request.method=='POST':
#         form = TestForm(request.POST, instance=post)
#         if form.is_valid():
#             post=form.save()
#             return redirect('post_detail', pk=post.pk)
#     else:
#         form = TestForm(instance=post)
#     return render(request, 'linkoapp/post_redit_form.html', {'form':form})

class CommentEdit(UpdateView):
    model= Comment
    fields=['post','author','content']
    template_name= 'linkoapp/comment_edit_form.html'
    success_url='/comments/'

class PortraitEdit(UpdateView):
    model= Portrait
    fields=['location','first_name','last_name','email','photo_url','previous_companies']
    template_name= 'linkoapp/portrait_edit_form.html'
    success_url='/profile/'

# ----Delete views----

class PostDelete(DeleteView):
    model=Post
    template_name='linkoapp/post_delete_form.html'
    success_url='/posts/'

class CommentDelete(DeleteView):
    model=Comment
    template_name='linkoapp/comment_delete_form.html'
    success_url='/posts'

class PortraitDelete(DeleteView):
    model=Portrait
    template_name='linkoapp/portrait_delete_form.html'
    success_url='/home'


