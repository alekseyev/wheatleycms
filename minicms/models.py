from django.contrib.sitemaps import Sitemap
from django.db import models
from tinymce import models as tinymce_models

class BaseContent(models.Model):
    title = models.CharField(max_length=200)
    content = tinymce_models.HTMLField(blank=True)
    last_update = models.DateTimeField(auto_now=True)

    @property
    def rendered_content(self):
        from django.utils.safestring import mark_safe
        return mark_safe(self.content)

    class Meta:
        abstract = True

class Page(BaseContent):
    url = models.CharField('URL', max_length=200)
    show_share_buttons = models.BooleanField(default=True,
        help_text='Show buttons for sharing this page on Twitter, Facebook, etc.')
    published = models.BooleanField(default=True)

    def __unicode__(self):
        return u"%s -- %s" % (self.url, self.title)

    def get_absolute_url(self):
        return self.url

class Block(models.Model):
    name = models.CharField(max_length=200)
    content = tinymce_models.HTMLField(blank=True)

    def __unicode__(self):
        return self.name

class Menu(models.Model):
    name = models.CharField(max_length=200)
    content = models.TextField(blank=True)

    def __unicode__(self):
        return self.name

class PagesSitemap(Sitemap):
    changefreq = "daily"

    def items(self):
        return Page.objects.filter(published=True)[:2000]

    def lastmod(self, obj):
        return obj.last_update
