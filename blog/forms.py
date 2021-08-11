from django import forms
from django.core.exceptions import ValidationError
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
            'tags': forms.SelectMultiple(attrs={'class': 'form-select'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
        }

        def __init__(self, *args, **kwargs):
            super(PostForm, self).__init__(*args, **kwargs)

            self.fields['content'].widget.attrs.update(
                {'class': 'form-control', 'placeholder': '# Markdown Supported'})

        # def clean(self):
        #     tags = self.cleaned_data.get('tags')
        #     print(tags)
        #     if len(tags[:]) > 3:
        #         raise ValidationError("You can't select more than 3 items.")
        #     return self.cleaned_data
