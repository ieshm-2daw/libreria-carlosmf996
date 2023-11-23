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

    class Disponibilidad(models.TextChoices):
        disponible = 'DIS', 'Disponible'
        prestado = 'PRE' , 'Prestado'
        enProceso = 'PDP', 'En proceso de prestamo'

    titulo = models.CharField(max_length=20)
    autor = models.CharField(max_length=250)
    editorial = models.CharField(max_length=20)
    fecha_publicacion = models.DateField()
    genero = models.CharField(max_length=15)
    isbn = models.CharField(max_length=17)
    resumen = models.TextField()
    disponibilidad = models.CharField(max_length=3, 
                                      choices=Disponibilidad.choices)
    portada = models.ImageField()

    def __str__(self):
        return self.titulo

class Autor(models.Model):
    nombre = models.CharField(max_length=50)
    biografia = models.TextField()
    web = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Editorial(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=200)
    web = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Prestamo(models.Model):
    