from django.shortcuts import render
from django.views.generic import ListView
from .models import Libro, Usuario, Autor, Editorial, Prestamo

# Create your views here.

class LibroList(ListView):
    
    model = Libro
    template_name = 'biblioteca/libro_list.html'