from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^login/$', 'django.contrib.auth.views.login'),
    (r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    (r'^register/$', 'accounts.views.register'),
    (r'^reset/$', 'django.contrib.auth.views.password_reset'),
    (r'^reset/done/$', 'django.contrib.auth.views.password_reset_done'),
    (r'^reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', 'django.contrib.auth.views.password_reset_confirm'),
    (r'^reset/complete/$', 'django.contrib.auth.views.password_reset_complete'),
)