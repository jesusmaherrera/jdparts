from common import *
from local_settings import DATABASES, JDPARTS_MODULES

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DJANGO_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'autocomplete_light',
    'dajaxice',
)

# Combine all the apps in the django variable INSTALLED_APPS
INSTALLED_APPS = DJANGO_APPS + JDPARTS_MODULES

ROOT_URLCONF = 'jdpartsmx.urls.prod'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    (RUTA_PROYECTO + '/static/'),
)