from django.conf.urls.defaults import *

urlpatterns = patterns('blog.views',
    (r'^review/(?P<review_key>.*)$', 'review'),
    (r'^add(?P<blog_url>.*)$', 'add_post'),
)
