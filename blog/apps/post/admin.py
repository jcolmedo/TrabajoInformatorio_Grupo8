from django.contrib import admin
from .models import *

class CategoriaAdmin(admin.ModelAdmin):
    ordering=("id", "nombre", "activado", "fecha_creacion")
    search_fields=("id", "nombre", "activado", "fecha_creacion")
    list_display=("id", "nombre", "activado", "fecha_creacion")
    list_filter=("activado",)



class PostAdmin(admin.ModelAdmin):
    ordering=("id","titulo","resumen","texto","imagen","categoria","publicado","fecha_creacion","usuario")
    search_fields=("id","titulo","resumen","texto","imagen","categoria","publicado","fecha_creacion")
    list_display=("titulo","resumen","imagen","categoria","publicado","fecha_creacion","usuario")
    #como categoria es en realidad la clase, para tomar el nombre tenemos que usar el __
    list_filter=("categoria__nombre", "publicado")

class ComentarioAdmin(admin.ModelAdmin):
    ordering=("id", "nombre", "post", "fecha_creacion")
    search_fields=("id", "nombre", "post", "fecha_creacion")
    list_display=("id", "nombre", "post", "fecha_creacion")
    list_filter=("post","nombre")






admin.site.register(Comentarios,ComentarioAdmin)
admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Post,PostAdmin)


