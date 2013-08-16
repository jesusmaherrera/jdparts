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

INSTALLED_APPS = DJANGO_APPS + JDPARTS_MODULES

ROOT_URLCONF = 'jdpartsmx.urls.dev'

STATICFILES_DIRS = (
    (RUTA_PROYECTO + '/static/'),
)
