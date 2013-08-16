from django.conf.urls import patterns, url
from django.views import generic
from jdpartsmx.apps.catalogo import views

urlpatterns = patterns('',
    (r'^articulos/$', views.articulos_view),
    (r'^articulos/(?P<clave>\w+)/', views.articulos_view),
)