from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, FormView
from .models import Libro, Usuario, Autor, Editorial, Prestamo

# Create your views here.

class LibroList(ListView):
    
    model = Libro
    template_name = 'biblioteca/libro_list.html'

class New(FormView):

    model = Libro
    template_name = 'biblioteca/new.html'
    fields = []
    success_url = reverse_lazy("libro_list")

class LibroDetails(DetailView):

    model = Libro
    template_name = 'biblioteca/libro_details.html'

class LibroDelete(DeleteView):

    model = Libro
    template_name = 'biblioteca/libro_delete.html'
    success_url = reverse_lazy("libro_list")