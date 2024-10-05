from django.forms import forms
from django.forms import ModelForm

from .models import Post
class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'author']
