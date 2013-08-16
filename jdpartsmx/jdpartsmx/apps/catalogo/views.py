
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext

#Paginacion
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# user autentication
from django.contrib.auth.decorators import login_required, permission_required

from models import *
from forms import *

def index_view(request, template_name='index.html'):
    return render_to_response(template_name, {}, context_instance=RequestContext(request))
    
def articulos_view(request, clave='', template_name='/catalogo/articulos.html'):
    if request.method =='POST':    
        filtro_form = filtroarticulos_form(request.POST)
        if filtro_form.is_valid():
            clave = filtro_form.cleaned_data['clave']
            nombre = filtro_form.cleaned_data['nombre']
            if clave != '':
                articulos_list = Articulo.objects.filter(clave__icontains=clave).order_by('-nombre')
            elif nombre != '':
                articulos_list = Articulo.objects.filter(nombre__icontains=nombre).order_by('-nombre')
            else:
                articulos_list = Articulo.objects.all().order_by('-id')
    else:
        filtro_form = filtroarticulos_form()
        if clave != '':
            articulos_list = Articulo.objects.filter(clave__icontains=clave).order_by('-nombre')
            filtro_form.clave = clave
        else:
            articulos_list = Articulo.objects.all().order_by('-id')
        filtro_form = filtroarticulos_form()

    paginator = Paginator(articulos_list, 30) # Muestra 5 inventarios por pagina
    page = request.GET.get('page')

    #####PARA PAGINACION##############
    try:
        articulos = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        articulos = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        articulos = paginator.page(paginator.num_pages)

    c = {'articulos':articulos, 'filtro_form':filtro_form,}
    return render_to_response(template_name, c, context_instance=RequestContext(request))
