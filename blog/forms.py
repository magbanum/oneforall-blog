from django import forms
from django.forms.models import ModelForm
from .models import Post
from markdownx.fields import MarkdownxFormField


class PostForm(ModelForm):
    content = MarkdownxFormField()

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags', 'status']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'tags': forms.Select(attrs={'class': 'form-select'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
        }

        def __init__(self, *args, **kwargs):
            super(PostForm, self).__init__(*args, **kwargs)

            self.fields['content'].widget.attrs.update({'class': 'form-control', 'placeholder': '# Markdown Supported'})
            



class PostEditForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags', 'status']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'tags': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }
