
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.views import generic
from dajaxice.core import dajaxice_autodiscover, dajaxice_config
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from jdpartsmx.settings.prod import JDPARTS_MODULES 

dajaxice_autodiscover()
import autocomplete_light
autocomplete_light.autodiscover()

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^catalogo/', include('jdpartsmx.apps.catalogo.urls', namespace='catalogo')),
    url(r'^$', 'jdpartsmx.apps.catalogo.views.index_view'),
    #imagenes
    url(r'^media/(?P<path>.*)$','django.views.static.serve',
        {'document_root':settings.MEDIA_ROOT,}
    ),
)

urlpatterns += staticfiles_urlpatterns()