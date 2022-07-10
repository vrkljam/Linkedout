from django import forms
from .models import Post, Comment, Profile

class PostForm(forms.ModelForm):
    class Meta:
        model =Post
        fields=('username','title','post_content')

class ProfileForm(forms.ModelForm):
        model =Profile
        fields="__all__"
        # user_from_model=forms.CharField(max_length=50)
        # is_retired=forms.BooleanField()
        # previous_companies=forms.Textarea()
        # location=forms.CharField(max_length=100)
        # photo_url=forms.Textarea()
        
        
class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields = ('post','author','content',)
