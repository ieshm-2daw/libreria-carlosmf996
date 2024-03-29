from django.urls import path
'''from django.contrib.auth.views'''
from . import views
from .views import LibroList, New, LibroDetails, LibroDelete, Edit, Reserva, Devolver, MisLibros

urlpatterns = [
    path('',LibroList.as_view(), name='libro_list'),
    path('new', New.as_view(), name ='new'),
    path('libro/<int:pk>/', LibroDetails.as_view(), name='libro_details'),
    path('libro/<int:pk>/delete/', LibroDelete.as_view(), name='libro_delete'),
    path('libro/<int:pk>/edit/', Edit.as_view(), name='libro_edit'),
    path('libro/<int:pk>/reserva/', Reserva.as_view(), name='libro_reserva'),
    path('libro/<int:pk>/devolver/', Devolver.as_view(), name='libro_devolver'),
    path('libro/mis_libros/', MisLibros.as_view(), name='mis_libros'),
]