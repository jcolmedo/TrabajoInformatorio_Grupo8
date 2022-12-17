from django.shortcuts import render
from apps.post.models import *

def index(request):
    posts= Post.objects.all().order_by("-fecha_creacion")[:3:]
    return render(request, "index.html",{"posts":posts})


