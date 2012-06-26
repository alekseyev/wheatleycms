from django import forms
from bootstrap.forms import BootstrapModelForm
from .models import Post
from images.widgets import WYSIWYG_Images

class PostForm(BootstrapModelForm):
    class Meta:
        model = Post
        exclude = ('blog', 'author', 'published_on', 'review_key')
        widgets = {
            'content': WYSIWYG_Images(),
        }
