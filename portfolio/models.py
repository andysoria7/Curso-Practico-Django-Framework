from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo")
    description = models.TextField(verbose_name="Descripcion")
    image = models.ImageField(verbose_name="Imagen", upload_to='projects') # uplodad_to sirve para que guarde todas las imagenes de Project, en un directorio projects dentro de media.
    link = models.URLField(verbose_name="Direccion web", null=True, blank=True) # Para que pueda estar vacio y no de error.
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion")
    
    class Meta: # La tipica clase meta para añadir meta datos extendidos.
        verbose_name = 'proyecto'
        verbose_name_plural = 'proyectos'
        ordering = ["-created"] # Para que ordene desde el mas nuevo al mas antiguo se le pone un - y luego created.
        
    def __str__(self):
        return self.title
        
        
        
        
        
        
    
