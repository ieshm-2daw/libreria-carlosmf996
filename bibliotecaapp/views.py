from datetime import date, timedelta
from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from .models import Libro, Usuario, Autor, Editorial, Prestamo
from .forms import LibroForm
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class LibroList(LoginRequiredMixin, ListView):
    
    model = Libro
    template_name = 'biblioteca/libro_list.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:

        context = super().get_context_data(**kwargs)

        autores = self.request.GET.get('autor')

        context['autores'] = Autor.objects.all()
        context['libros_disponibles'] = Libro.objects.filter(disponibilidad = "DIS")
        context['libros_prestados'] = Libro.objects.filter(disponibilidad = "PRE")

        if autores != "all" and autores != None:
            autor = Autor.objects.get(nombre = autores)
            context['libros_disponibles'] = context['libros_disponibles'].filter(autor=autor)
            context['libros_prestados'] = context['libros_prestados'].filter(autor=autor)

        ##filtro_titulo1 = self.request.GET.get('filtro1')  --> CREA UNA CONDICION PARA EL FILTRO
        ##queryset = Libro.objects.filter(disponibilidad = 'DIS')   --> CREA UN QUERYSET (ARRAY) CON TODOS LOS LIBROS DISPONIBLES
        ##self.queryset = self.queryset.filter(titulo__icontains = filtro_titulo1)   --> APLICA AL QUERYSET ANTERIOR EL FILTRO CREADO

        return context

    ##queryset = Libro.objects.filter(disponibilidad = "DIS")

    ##def get_queryset(self):
    ##  return Libro.objects.filter(disponibilidad="DIS")
    

'''class New(View):
        
    def get(self, request):
        form=LibroForm()
        return render(request, 'biblioteca/new.html', {'form': form})
    
    def post(self, request):
        form=LibroForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('libro_list')
        return render(request, 'biblioteca/new.html', {'form': form})'''

class New(LoginRequiredMixin, CreateView):

    model = Libro
    fields = ["titulo", "autor", "editorial", "rating", "fecha_publicacion", "genero", "isbn", "resumen", "disponibilidad", "portada"]
    template_name = 'biblioteca/new.html'
    success_url = reverse_lazy("libro_list")

class LibroDetails(LoginRequiredMixin, DetailView):

    model = Libro
    template_name = 'biblioteca/libro_details.html'

class LibroDelete(LoginRequiredMixin, DeleteView):

    model = Libro
    template_name = 'biblioteca/libro_delete.html'
    success_url = reverse_lazy("libro_list")

class Edit(LoginRequiredMixin, UpdateView):

    model = Libro
    fields = ["titulo", "autor", "editorial", "rating", "fecha_publicacion", "genero", "isbn", "resumen", "disponibilidad", "portada"]
    template_name = 'biblioteca/libro_edit.html'
    success_url = reverse_lazy("libro_list")


class Reserva(LoginRequiredMixin, View):
    
    def get(self, request, pk):
        libro = get_object_or_404(Libro, pk=pk)
        return render(request, 'biblioteca/libro_reserva.html', {'libro': libro})

    def post(self, request, pk):
        libro = get_object_or_404(Libro, pk=pk)
        libro.disponibilidad = 'PRE'
        libro.save()
        
        fecha_devuelta = date.today() + timedelta(days=15)

        Prestamo.objects.create(
            libro=libro,
            fechaPrestamo=date.today(),
            fechaDevolucion=fecha_devuelta,
            usuario=request.user,
            estado='PRE'
        )

        return redirect('libro_list')
    
class Devolver(LoginRequiredMixin, View):

    def get(self, request, pk):
        libroPrestado = get_object_or_404(Libro, pk=pk, disponibilidad='PRE')
        prestamo = Prestamo.objects.filter(libro=libroPrestado, usuario=request.user).first()

        return render(request, 'biblioteca/libro_devolver.html', {'prestamo': prestamo})

    def post(self, request, pk):
        libro = get_object_or_404(Libro, pk=pk, disponibilidad='PRE')
        prestamo = Prestamo.objects.filter(libro=libro, usuario=request.user, estado='PRE').first()

        prestamo.fechaDevolucion = date.today()
        prestamo.estado = 'DEV'
        libro.disponibilidad = 'DIS'

        prestamo.save()
        libro.save()

        return redirect('libro_list')
    
    
class MisLibros(LoginRequiredMixin, ListView):
    
    model = Prestamo
    template_name = 'biblioteca/mis_libros.html'


    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:

        context = super().get_context_data(**kwargs)
        context['fecha_hoy'] = date.today()

        context['libros_disponibles_usuario'] = Prestamo.objects.filter(usuario=self.request.user, estado='PRE').order_by('fechaDevolucion')
        context['libros_devueltos_usuario'] = Prestamo.objects.filter(usuario=self.request.user, estado='DEV')

        return context