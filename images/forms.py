from django import forms
from bootstrap.forms import BootstrapModelForm

from models import Image

class ImageUploadForm(BootstrapModelForm):
    class Meta:
        model = Image