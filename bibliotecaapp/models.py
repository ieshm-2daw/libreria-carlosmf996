from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Usuario(AbstractUser):
    dni = models.CharField(max_length=9)
    direccion = models.CharField(max_length=200)
    telefono = models.IntegerField(max_length=9)

    def __str__(self):
        return self.dni

class Libro(models.Model):
    titulo = models.CharField(max_length=20)
    autor = models.CharField(max_length=250)
    editorial = models.CharField(max_length=20)
    fecha_publicacion = models.DateField()
    genero = models.CharField(max_length=15)
    isbn = models.CharField(max_length=17)