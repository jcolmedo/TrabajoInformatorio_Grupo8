from django.urls import path
from apps.nosotros import views


urlpatterns = [
    path('nosotros/', views.nosotros, name='nosotros'),
]
