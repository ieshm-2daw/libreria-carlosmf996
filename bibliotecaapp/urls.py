from django.urls import path
from . import views
from .views import LibroList

urlpatterns = [
    path('',LibroList.as_view(), name='libro_list'),
]