from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model =Post
        fields=('username', 'name_of_user','title','post_content')

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields = ('post','author','content',)
