from django.urls import path
from . import views
from .views import LibroList, New, LibroDetails, LibroDelete, Edit

urlpatterns = [
    path('',LibroList.as_view(), name='libro_list'),
    path('new', New.as_view(), name ='new'),
    path('libro/<int:pk>/', LibroDetails.as_view(), name='libro_details'),
    path('libro/<int:pk>/delete/', LibroDelete.as_view(), name='libro_delete'),
    path('libro/<int:pk>/edit/', Edit.as_view(), name='libro_edit'),
]