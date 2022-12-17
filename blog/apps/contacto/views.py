from django.shortcuts import render
from .forms import *

def contacto(request):
	data={
		"contactoForm":ContactoForm()
	}
	if request.method=="POST":
		formulario=ContactoForm(data=request.POST)
		if formulario.is_valid():
			formulario.save()
			data["mensaje"]="Enviado OK"
		else:
			data["contactoForm"] = formulario

	return render(request,"contacto/contacto.html",data)

def verMensaje(request,id):
	if request.method=="GET":
		mensaje=Contacto.objects.get(pk=id)
		mensaje.no_leido=False
		mensaje.save()
		context={
			"mensaje":mensaje
		}
	

	return render(request,"contacto/ver_mensaje.html",context )

def verTodosMensaje(request):
	
	mensajes=Contacto.objects.all().order_by("-fecha_creacion")
	context={
			"mensajes":mensajes
	}
	return render(request,"contacto/ver_todos.html",context )

	


