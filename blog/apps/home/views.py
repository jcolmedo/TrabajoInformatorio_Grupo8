from django.shortcuts import render
from apps.post.models import *

def index(request):
    posts= Post.objects.all()[:3:]
    return render(request, "index.html",{"posts":posts})


