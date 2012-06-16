from django import forms
from bootstrap.forms import BootstrapModelForm
from .models import Post
from wysihtml5.widgets import WYSIWYG

class PostForm(BootstrapModelForm):
    class Meta:
        model = Post
        exclude = ('blog', 'author', 'published_on', 'review_key')
        widgets = {
            'content': WYSIWYG(),
        }
