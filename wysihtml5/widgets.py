from django import forms
from django.utils.safestring import mark_safe

class WYSIWYG(forms.Textarea):
    def render(self, name, value, attrs=None):
        if not attrs: 
            attrs = {}
        attrs['class'] = attrs.get('class', '') + ' wysihtml5-widget'
        return super(WYSIWYG, self).render(name, value, attrs)

    class Media:
        js = (
            'wysihtml5/wysihtml5-0.3.0-wheatley.js',
            'wysihtml5/bootstrap-wysihtml5-0.0.2.js',
            'wysihtml5/init-wysihtml5.js'
        )
        css = {
            'all': ('wysihtml5/bootstrap-wysihtml5-0.0.2.css',)
        }