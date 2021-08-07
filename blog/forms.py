from django import forms
from django.forms.models import ModelForm
from .models import Post
class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'author', 'content', 'tags', 'status']

        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control'}),
            'author' : forms.Select(attrs={'class': 'form-control'}),
            'content' : forms.Textarea(attrs={'class': 'form-control'}),
            'tags' : forms.Select(attrs={'class': 'form-control'}),
            'status' : forms.Select(attrs={'class': 'form-control'}),
        }

class PostEditForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags', 'status']

        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control'}),
            'content' : forms.Textarea(attrs={'class': 'form-control'}),
            'tags' : forms.Select(attrs={'class': 'form-control'}),
            'status' : forms.Select(attrs={'class': 'form-control'}),
        }

