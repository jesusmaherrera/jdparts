from django.db import models

class Articulo(models.Model):
    clave = models.CharField(max_length=20)
    nombre = models.CharField(max_length=100, blank=True, null=True,)
    precio = models.DecimalField(max_digits=18, decimal_places=2)
    imagen = models.ImageField(blank=True, null=True, upload_to='articulos')
    
    def __unicode__(self):
        return u'%s' % self.nombre
