from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):

    sexo = models.CharField(max_length=30, blank=True, null=False, choices=(('masculino', 'Masculino'),
                                                                            ('femenino', 'Femenino'),
                                                                            ('otro', 'Otro')))
    provincia = models.CharField(max_length=50, null=True)
    ciudad = models.CharField(max_length=50, null=False)
    descripcion_propia = models.CharField(max_length=2000, null=True)




