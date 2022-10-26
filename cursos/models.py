from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
# Create your models here.



class Lenguaje(models.Model):

    Nombre = models.CharField(max_length=50)

    Historia = models.TextField(max_length=300)
## el siguiente comando sirve para que no te aparezca el object en lugar del nombre 
    def __str__(self):
        return self.Nombre


class Curso(models.Model):
    Nombre = models.CharField(max_length=50)

    Descripcion = models.TextField(max_length=300)

    Creador = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    AñosExperiencia = models.PositiveIntegerField(null = True, blank = True)

    Lenguaje = models.ForeignKey(
        Lenguaje,
        on_delete=models.CASCADE,
    )

    Horas = models.PositiveIntegerField(null = True, blank = True)

    Fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Nombre

    def get_absolute_url(self):
        return reverse('curso_detalle', args=(str(self.id)))

   
class Comentario(models.Model):
    Curso = models.ForeignKey(
        Curso,
        on_delete=models.CASCADE,
        related_name='comentarios',

    )
    comentario = models.CharField(max_length=200)
    autor = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        
    )

    def __str__(self):
        return self.comentario

    def get_absolute_url(self):
        return reverse('lista_curso')