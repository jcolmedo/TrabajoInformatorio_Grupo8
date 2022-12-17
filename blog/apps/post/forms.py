from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms import fields
from django.forms.forms import Form
from .models import *

class PostForm(forms.ModelForm):
    class Meta:
        model= Post
        fields= ["titulo","resumen","texto","imagen","categoria","usuario"]

class CategForm(forms.ModelForm):
    class Meta:
        model= Categoria
        fields= ["nombre",]

class ComentForm(forms.ModelForm):
    contenido=forms.CharField(widget=forms.Textarea(attrs={"row":"4",}))
    
    class Meta:
        model = Comentarios
        fields=["contenido",]