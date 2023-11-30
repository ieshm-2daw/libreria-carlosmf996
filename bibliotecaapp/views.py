from datetime import date
from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from .models import Libro, Usuario, Autor, Editorial, Prestamo
from .forms import LibroForm


# Create your views here.

class LibroList(ListView):
    
    model = Libro
    template_name = 'biblioteca/libro_list.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:

        context = super().get_context_data(**kwargs)

        context['libros_disponibles'] = Libro.objects.filter(disponibilidad = "DIS")
        context['libros_prestados'] = Libro.objects.filter(disponibilidad = "PRE")

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

class New(CreateView):

    model = Libro
    fields = ["titulo", "autor", "editorial", "rating", "fecha_publicacion", "genero", "isbn", "resumen", "disponibilidad", "portada"]
    template_name = 'biblioteca/new.html'
    success_url = reverse_lazy("libro_list")

class LibroDetails(DetailView):

    model = Libro
    template_name = 'biblioteca/libro_details.html'

class LibroDelete(DeleteView):

    model = Libro
    template_name = 'biblioteca/libro_delete.html'
    success_url = reverse_lazy("libro_list")

class Edit(UpdateView):

    model = Libro
    fields = ["titulo", "autor", "editorial", "rating", "fecha_publicacion", "genero", "isbn", "resumen", "disponibilidad", "portada"]
    template_name = 'biblioteca/libro_edit.html'
    success_url = reverse_lazy("libro_list")


class Reserva(DetailView):

    model = Libro
    fields = ["titulo", "autor", "editorial"]
    template_name = 'biblioteca/libro_reserva.html'

class ConfirmarReserva(View):

    def get(self, request, libro_id):
        libro = Libro.objects.get(pk=libro_id)
        return render(request, 'biblioteca/libro_list.html', {'libro': libro})

    def post(self, request, libro_id):
        libro = Libro.objects.get(pk=libro_id)

        prestamo = Prestamo(
            titulo=libro,
            fechaPrestamo=date.today(),
            fechaDevolucion=None,  
            usuario=request.user,
            estado='PRE'  
        )
        prestamo.save()

        return redirect('libro_list')
