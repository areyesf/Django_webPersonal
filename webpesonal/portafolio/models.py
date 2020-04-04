from django.db import models

# Create your models here.
class Projecto(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="titulo")
    img_link = models.URLField(verbose_name="Url imagen")
    descripcion = models.TextField(verbose_name="Descripción")
    link = models.URLField(verbose_name="URL Sitio Web")
    fch_creado = models.DateField(auto_now_add=True, verbose_name="Fecha Creación") 
    fch_mod = models.DateField(auto_now=True, verbose_name="Fecha Creación")

    class Meta:
        ordering=["-fch_creado"]

    def __str__(self):
        return self.titulo
