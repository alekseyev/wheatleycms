from django.db import models
from django.utils.safestring import mark_safe
from django.utils.importlib import import_module
from django.conf import settings

_backend_cache = None

def _load_backend():
    global _backend_cache
    if _backend_cache is None:  
        module_name, func_name = settings.IMAGES_BACKEND.rsplit('.', 1)
        _backend_cache = getattr(import_module(module_name), func_name)()    
    return _backend_cache

class Image(models.Model):
    image_inner = models.FileField(upload_to='img/')

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
        return mark_safe("<img src='%s'/>" % self.url())

    def thumbnail(self, size=200):
        return mark_safe("<img src='%s'/>" % self.thumbnail_url(size))

