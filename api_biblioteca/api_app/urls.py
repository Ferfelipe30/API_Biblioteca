from django.urls import path
from .views import (
    AutorList, CrearAutor, ActualizarAutor, EliminarAutor,
    EditorialList, CrearEditorial, ActualizarEditorial, EliminarEditorial
)

urlpatterns = [
    path('autores/', AutorList.as_view(), name='autor-list'),
    path('autores/crear/', CrearAutor.as_view(), name='autor-crear'),
    path('autores/<int:pk>/actualizar/', ActualizarAutor.as_view(), name='autor-actualizar'),
    path('autores/<int:pk>/eliminar/', EliminarAutor.as_view(), name='autor-eliminar'),
    path('editoriales/', EditorialList.as_view(), name='editorial-list'),
    path('editoriales/crear/', CrearEditorial.as_view(), name='editorial-crear'),
    path('editoriales/<int:pk>/actualizar/', ActualizarEditorial.as_view(), name='editorial-actualizar'),
    path('editoriales/<int:pk>/eliminar/', EliminarEditorial.as_view(), name='editorial-eliminar'),
]