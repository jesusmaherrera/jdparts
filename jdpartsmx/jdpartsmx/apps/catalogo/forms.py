#encoding:utf-8
from django import forms
from models import *
import autocomplete_light

class filtroarticulos_form(forms.Form):
    clave   = forms.CharField(max_length=100,  widget=forms.TextInput(attrs={'class':'input-small', 'placeholder':'Clave...'}),required=False)
    nombre  = forms.CharField(max_length=100,  widget=forms.TextInput(attrs={'class':'input-small', 'placeholder':'Nombre...'}),required=False)
    # articulo = forms.ModelChoiceField(required= False, queryset=Articulo.objects.all().order_by('nombre'),
    #     widget=autocomplete_light.ChoiceWidget('ArticulosAutocomplete'))
