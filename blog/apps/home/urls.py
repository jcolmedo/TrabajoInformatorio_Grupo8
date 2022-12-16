from django.urls import path
from apps.home import views


urlpatterns = [
    path('index/', views.index, name='home'),
]
