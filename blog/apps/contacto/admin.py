from django.contrib import admin
from .models import *



class ContactoAdmin(admin.ModelAdmin):
    ordering=("id","nombre","tipo_consulta","no_leido")
    search_fields=("id","nombre","tipo_consulta","no_leido")
    list_display=("id","nombre","tipo_consulta","no_leido","fecha_creacion")
    list_filter=("id","nombre","tipo_consulta","no_leido","fecha_creacion")



admin.site.register(Contacto,ContactoAdmin)
