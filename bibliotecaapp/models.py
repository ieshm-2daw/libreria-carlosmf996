from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator

# Create your models here.

class Usuario(AbstractUser):
    dni = models.CharField(max_length=9)
    direccion = models.CharField(max_length=200)
    telefono = models.IntegerField(max_length=9)

    def __str__(self):
        return self.dni
    
class Autor(models.Model):
    nombre = models.CharField(max_length=50)
    biografia = models.TextField()
    foto = models.ImageField(upload_to='retratos/', null=True, blank=True)

    def __str__(self):
        return self.nombre
    
class Editorial(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=200)
    web = models.URLField()

    def __str__(self):
        return self.nombre

class Libro(models.Model):

    disponibilidadChoices = (
        ('DIS', 'Disponible'),
        ('PRE' , 'Prestado'),
        ('PDP', 'En proceso de prestamo'),
    )

    titulo = models.CharField(max_length=20)
    autor = models.ManyToManyField(Autor)
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)
    rating = models.PositiveBigIntegerField(validators=[MaxValueValidator(5)])
    fecha_publicacion = models.DateField()
    genero = models.CharField(max_length=15)
    isbn = models.CharField(max_length=17)
    resumen = models.TextField()
    disponibilidad = models.CharField(max_length=3, 
                                      choices=disponibilidadChoices.choices, default='DIS')
    portada = models.ImageField(upload_to='portadas/', null=True, blank=True)

    def __str__(self):
        return self.titulo

class Prestamo(models.Model):

    estadoChoices = (
            ('DEV', 'Devuelto'),
            ('PRE' , 'Prestado'),
        )
 
    titulo = models.ForeignKey(Libro, on_delete=models.CASCADE)
    fechaPrestamo = models.DateField()
    fechaDevolucion = models.DateField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    estado = models.CharField(max_length=3, 
                              choices=estadoChoices.choices, default='DEV')

    def __str__(self):
        return self.titulo