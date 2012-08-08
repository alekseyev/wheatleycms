from django.db import models
from django.utils.safestring import mark_safe
from django.utils.importlib import import_module
from django.template.loader import render_to_string
from django.conf import settings
from django.utils.translation import ugettext as _

_backend_cache = None

def _load_backend():
    global _backend_cache
    if _backend_cache is None:  
        module_name, func_name = settings.IMAGES_BACKEND.rsplit('.', 1)
        _backend_cache = getattr(import_module(module_name), func_name)()    
    return _backend_cache

class Image(models.Model):
    image_inner = models.ImageField(_('Image'), upload_to='img/')
    created = models.DateTimeField(auto_now=True)
    caption = models.CharField(_('Caption'), max_length=256, blank=True)

    def __init__(self, *args, **kwargs):
        super(Image, self).__init__(*args, **kwargs)
        self.backend = _load_backend()

    def delete(self):
        image_inner.file.delete()
        super(Images, self).delete()

    def url(self):
        return self.backend.url(self.image_inner)

    def thumbnail_url(self, size=200):
        return self.backend.thumbnail_url(self.image_inner, size)

    def img(self):
        return render_to_string('images/image.html', 
            {'image_url': self.url(), 'caption': self.caption})
        #mark_safe("<img src='%s'/>" % self.url())

    def thumbnail(self, size=200):
        return render_to_string('images/thumbnail.html',
            {'image_url': self.url(), 'caption': self.caption, 
             'thumbnail_url': self.thumbnail_url(size)})
        #mark_safe("<img src='%s'/>" % self.thumbnail_url(size))

