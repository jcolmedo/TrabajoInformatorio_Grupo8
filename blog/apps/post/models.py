from django.db import models

from apps.usuario.models import *

class Categoria(models.Model):
    nombre=models.CharField(max_length=40, null=False, blank=False)
    activado=models.BooleanField(default=True)
    fecha_creacion=models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural="Categorias"
    
    def __str__(self):
        return str(self.nombre)
    def primaria(self):
        return int(self.pk)

class Post(models.Model):
    titulo= models.CharField(max_length=40,blank=False,null=False)
    resumen= models.CharField(max_length=140,blank=False,null=False)
    texto= models.TextField(max_length=600,blank=False,null=False)
    imagen=models.ImageField(upload_to="post", null=True)
    categoria= models.ForeignKey(Categoria, on_delete=models.CASCADE)
    publicado=models.BooleanField(default=True)
    fecha_creacion=models.DateField(auto_now_add=True)
    usuario=models.ForeignKey(Usuario,on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural="post"

    def __str__(self):
        return str(self.titulo)



