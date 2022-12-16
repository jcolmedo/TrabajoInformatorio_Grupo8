from django.urls import path, re_path
from .views import *

urlpatterns = [
    path("contacto/", contacto, name="contacto"),
    path("ver_todos/", verTodosMensaje, name="ver_todos" ),
    re_path("ver_mensaje/(?P<id>\d+)/$", verMensaje, name="ver_mensaje" )   
]