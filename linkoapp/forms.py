from dataclasses import fields
from django import forms
from .models import Post, Comment, Portrait, Buckets


class PostForm(forms.ModelForm):
    class Meta:
        model =Post
        fields=('username','title','post_content')
        
        
class PortraitForm(forms.ModelForm):
        model =Portrait
        fields=('user','first_name', 'last_name','previous_companies','photo_url','location',)
       
        
class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields = ('post','author','content',)

class BucketForm(forms.ModelForm):
    class Meta:
        model=Buckets
        fields=('title','complete')

