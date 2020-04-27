from django import forms
from .models import Post
from tinymce.models import HTMLField
from tinymce.widgets import TinyMCE


class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=100)
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = Post
        fields = ('title', 'content')
