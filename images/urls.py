from django.conf.urls.defaults import *

urlpatterns = patterns('images.views', 
    (r'^ajax/upload_post/$', 'ajax_upload_post'),
)