# -*- coding: utf-8 -*-

from django.contrib.messages import constants as message_constants

# The following takes care of auto-configuring the database. You might want to
# modify this to match your environment (i.e., without fallbacks).
try:
    from djangoappengine.settings_base import *
    has_djangoappengine = True
except ImportError:
    has_djangoappengine = False
    DEBUG = True
    TEMPLATE_DEBUG = DEBUG

    # Fall back to MongoDB if App Engine isn't used (note that other backends
    # including SQL should work, too)
    DATABASES = {
        'default': {
            'ENGINE': 'django_mongodb_engine',
            'NAME': 'test',
            'USER': '',
            'PASSWORD': '',
            'HOST': 'localhost',
            'PORT': 27017,
        }
    }

import os

# Activate django-dbindexer for the default database
DATABASES['native'] = DATABASES['default']
DATABASES['default'] = {'ENGINE': 'dbindexer', 'TARGET': 'native'}
AUTOLOAD_SITECONF = 'dbindexes'

SITE_NAME = 'GosuCMS Demo Site'
SITE_DESCRIPTION = ''
SITE_COPYRIGHT = ''

LANGUAGE_CODE='en'
USE_I18N = True
USE_L10N = True 

DISQUS_SHORTNAME = ''
GOOGLE_ANALYTICS_ID = ''
# Get the ID from the CSE "Basics" control panel ("Search engine unique ID")
GOOGLE_CUSTOM_SEARCH_ID = ''
# Set RT username for retweet buttons
TWITTER_USERNAME = ''
# In order to always have uniform URLs in retweets and FeedBurner we redirect
# any access to URLs that are not in ALLOWED_DOMAINS to the first allowed
# domain. You can have additional domains for testing.
ALLOWED_DOMAINS = ()

SECRET_KEY = '=r-$b*8hglm+858&9t043hlm6-&6-3d3vfc4((7yd0dbrakhvi'

INSTALLED_APPS = (
    'accounts', # needs to be above django.contrib.admin (template conficts)
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.contenttypes',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'urlrouter',
    'minicms',
    'blog',
    'disqus',
    'djangotoolbox',
    'google_analytics',
    'google_cse',
    'robots',
    'redirects',
    'autoload',
    'dbindexer',
    'utils',
    'wysihtml5',
)

if has_djangoappengine:
    # djangoappengine should come last, so it can override a few manage.py commands
    INSTALLED_APPS += ('djangoappengine',)
else:
    INSTALLED_APPS += ('django_mongodb_engine',)

TEST_RUNNER = 'djangotoolbox.test.CapturingTestSuiteRunner'

MIDDLEWARE_CLASSES = (
    # This loads the index definitions, so it has to come first
    'autoload.middleware.AutoloadMiddleware',

    'django.middleware.common.CommonMiddleware',
    'djangotoolbox.middleware.RedirectMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'urlrouter.middleware.URLRouterFallbackMiddleware',
)

URL_ROUTE_HANDLERS = (
    'minicms.urlroutes.PageRoutes',
    'blog.urlroutes.BlogRoutes',
    'blog.urlroutes.BlogPostRoutes',
    'redirects.urlroutes.RedirectRoutes',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'minicms.context_processors.cms',
)

TEMPLATE_DIRS = (os.path.join(os.path.dirname(__file__), 'templates'),)

if DEBUG: 
    STATIC_URL = '/devstatic/'
else:
    STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(os.path.dirname(__file__), 'sitestatic')

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

STATICFILES_DIRS = (
    os.path.join(os.path.dirname(__file__), 'static'),
)

ADMIN_MEDIA_PREFIX = '/static/admin/'

ROOT_URLCONF = 'urls'

NON_REDIRECTED_PATHS = ('/admin/',)

# When using django.contrib.messages, output messages with Twitter Bootstrap-friendly classes

MESSAGE_TAGS = {
    message_constants.DEBUG: '',
    message_constants.INFO: 'alert-info',
    message_constants.SUCCESS: 'alert-success',
    message_constants.WARNING: '',
    message_constants.ERROR: 'alert-error',
}

try:
    from settings_local import *
except ImportError:
    pass
