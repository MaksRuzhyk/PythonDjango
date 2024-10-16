from django.forms import forms
from django.forms import ModelForm

from .models import Post, Coment
class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

class CommentForm(ModelForm):
    class Meta:
        model = Coment
        fields = ['text']