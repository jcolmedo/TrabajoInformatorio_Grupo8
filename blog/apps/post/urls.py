from django.urls import path,re_path
from apps.post import views
from apps.post.views import *



urlpatterns = [
    path('crear_post/', views.crearPost, name="crear_post"),
    re_path("post/(?P<id>\d+)/$", leerPost, name="post" ),
    path('posteos/', views.home, name="posteos"),
    path("crear_categoria", views.crearCategoria, name="crear_categoria" ),
]