from django import forms
from .models import *

class ContactoForm(forms.ModelForm):
    class Meta:
        model= Contacto
        fields=["nombre","correo","tipo_consulta", "mensaje"]
        
