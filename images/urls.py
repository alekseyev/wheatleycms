from django.conf.urls.defaults import *

urlpatterns = patterns('images.views', 
    (r'^ajax/upload_post/$', 'ajax_upload_post'),
    (r'^ajax/images/$', 'ajax_list_images'),
    (r'^ajax/thumbnail/$', 'ajax_thumbnail_code'),
    (r'^ajax/get_upload_data/$', 'ajax_get_upload_data')
)