from django.db import models

opciones_consulta=[
    [0, "consulta"],
    [1 ,"reclamo"],
    [2, "sugerencia"],
    [3, "felicitaciones"],
]

class Contacto(models.Model):
    nombre=models.CharField(max_length=50)
    correo=models.EmailField()
    tipo_consulta=models.IntegerField(choices=opciones_consulta)
    mensaje=models.TextField(max_length=600, blank=True, null=True)
    no_leido=models.BooleanField(default=True)
    fecha_creacion=models.DateField(auto_now_add=True)

    
    def __str__(self) :
        return self.nombre