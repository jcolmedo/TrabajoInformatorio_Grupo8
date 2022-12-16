from django.urls import path
from .views import *


urlpatterns = [
    path('ver_perfil/', ver_perfil, name='ver_perfil'),
    path('editar_perfil/<int:usuario_id>', editar_perfil, name='editar_perfil'),
]