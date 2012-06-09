from django import forms

from widgets import WYSIWYG

class TestForm(forms.Form):
    text = forms.CharField(widget=WYSIWYG)