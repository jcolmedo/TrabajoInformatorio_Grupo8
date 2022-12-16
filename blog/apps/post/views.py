from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.utils.datastructures import MultiValueDictKeyError
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.views.generic import View
from django.db.models import Q


def crearPost(request):
    if request.method == "POST" : 
        post_form = PostForm(request.POST or None, request.FILES or None)
        if post_form.is_valid():
            post_form.save()
            return redirect("crear_post")
    else:
            post_form= PostForm()
    return render(request, "post/crear_post.html", {"post_form":post_form})

def leerPost(request,id):
    if request.method=="GET":
        post=Post.objects.get(pk=id)
        context={
            "post":post
        }
    pass
    return render(request, "post/post.html", context)


def home(request):
        queryset=request.GET.get("buscar")
        posts= Post.objects.filter(publicado=True)
        if queryset:
            posts=Post.objects.filter(
                Q(titulo__icontains= queryset) |
                Q(resumen__icontains=queryset) |
                Q(categoria__nombre__icontains=queryset)
            ).distinct()

        return render(request, "post/posteos.html" , {"posts":posts})

def crearCategoria(request):
    if request.method == "POST" : 
        categoria = CategForm(request.POST or None)
        if categoria.is_valid():
            categoria.save()
            return redirect("crear_post")
    else:
            categoria= CategForm()
    return render(request, "post/crear_categoria.html", {"categoria":categoria})







