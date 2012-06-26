from django import forms
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext as _
from django.template.loader import render_to_string
from filetransfers.api import prepare_upload
from django.core.urlresolvers import reverse

from wysihtml5.widgets import WYSIWYG
from .forms import ImageUploadForm

class WYSIWYG_Images(WYSIWYG):
    def render(self, name, value, attrs=None):
        context = {
            'upload_form': ImageUploadForm(),
            'view_url': reverse('images.views.ajax_upload_post'),
        }
        context['upload_url'], context['upload_data'] = prepare_upload(None, context['view_url'])
        output = render_to_string('images/upload_widget.html', context)
        output += super(WYSIWYG_Images, self).render(name, value, attrs)
        return output

    class Media:
        js = ('images/jquery.form.js', 'images/imageupload.js')
