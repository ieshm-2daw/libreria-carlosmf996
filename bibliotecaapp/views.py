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

class New(View):
        
    def get(self, request):
        form=LibroForm()
        return render(request, 'biblioteca/new.html', {'form': form})
    
    def post(self, request):
        form=LibroForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('libro_list')
        return render(request, 'biblioteca/new.html', {'form': form})

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