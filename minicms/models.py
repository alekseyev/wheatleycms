from django.contrib.sitemaps import Sitemap
from django.db import models
from django.utils.translation import ugettext as _

class BaseContent(models.Model):
    title = models.CharField(_('Title'), max_length=200)
    content = models.TextField(_('Content'), blank=True)
    last_update = models.DateTimeField(_('Last update'), auto_now=True)

    @property
    def rendered_content(self):
        from django.utils.safestring import mark_safe
        return mark_safe(self.content)

    class Meta:
        abstract = True

class Page(BaseContent):
    url = models.CharField(_('URL'), max_length=200)
    published = models.BooleanField(_('Published'), default=True)

    def __unicode__(self):
        return u"%s -- %s" % (self.url, self.title)

    def get_absolute_url(self):
        return self.url

class Block(models.Model):
    name = models.CharField(_('Name'), max_length=200)
    content = models.TextField(_('Content'), blank=True)

    def __unicode__(self):
        return self.name

class Menu(models.Model):
    name = models.CharField(_('Name'), max_length=200)
    content = models.TextField(_('Content'), blank=True)

    def __unicode__(self):
        return self.name

class PagesSitemap(Sitemap):
    changefreq = "daily"

    def items(self):
        return Page.objects.filter(published=True)[:2000]

    def lastmod(self, obj):
        return obj.last_update
