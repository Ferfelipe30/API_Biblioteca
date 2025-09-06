from django.urls import path
from .views import (
    AutorList, CrearAutor, ActualizarAutor, EliminarAutor
)

urlpatterns = [
    path('autores/', AutorList.as_view(), name='autor-list'),
    path('autores/crear/', CrearAutor.as_view(), name='autor-crear'),
    path('autores/<int:pk>/actualizar/', ActualizarAutor.as_view(), name='autor-actualizar'),
    path('autores/<int:pk>/eliminar/', EliminarAutor.as_view(), name='autor-eliminar'),
    
]