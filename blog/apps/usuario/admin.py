from django.contrib import admin
from .models import *

class UsuarioAdmin(admin.ModelAdmin):
	list_display = ('id','username','first_name','last_name','sexo','provincia','ciudad')
	list_filter = ('sexo','provincia','ciudad')

admin.site.register(Usuario,UsuarioAdmin)
