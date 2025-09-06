from django.urls import path
from .views import (
    AutorList, CrearAutor, ActualizarAutor, EliminarAutor,
    EditorialList, CrearEditorial, ActualizarEditorial, EliminarEditorial,
    LibroList, CrearLibro, ActualizarLibro, EliminarLibro, LibroFiltro,
    MiembroList, CrearMiembro, ActualizarMiembro, EliminarMiembro,
    PrestamoList, CrearPrestamo, ActualizarPrestamo, EliminarPrestamo,

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
    path('libros/', LibroList.as_view(), name='libro-list'),
    path('libros/crear/', CrearLibro.as_view(), name='libro-crear'),
    path('libros/<int:pk>/actualizar/', ActualizarLibro.as_view(), name='libro-actualizar'),
    path('libros/<int:pk>/eliminar/', EliminarLibro.as_view(), name='libro-eliminar'),
    path('libros/filtroAutor/<int:autor_id>/', LibroFiltro.as_view(), name='libro-filtro-1'),
    path('libros/filtroEditorial/<int:editorial_id>/', LibroFiltro.as_view(), name='libro-filtro-2'),
    path('libros/filtro/<int:autor_id>/<int:editorial_id>/', LibroFiltro.as_view(), name='libro-filtro-3'),

    # rutas de miembros :

    path('miembros/', MiembroList.as_view(), name='miembro-list'),
    path('miembros/crear/', CrearMiembro.as_view(), name='miembro-crear'),
    path('miembros/<int:pk>/actualizar/', ActualizarMiembro.as_view(), name='miembro-actualizar'),
    path('miembros/<int:pk>/eliminar/', EliminarMiembro.as_view(), name='miembro-eliminar'),
    path('miembros/<int:miembro_id>/prestamos/', PrestamoList.as_view(), name='prestamos-por-miembro'),
    # rutas de prestamos :
    
    path('prestamos/', PrestamoList.as_view(), name='prestamo-list'),
    path('prestamos/crear/', CrearPrestamo.as_view(), name='prestamo-crear'),
    path('prestamos/<int:pk>/actualizar/', ActualizarPrestamo.as_view(), name='prestamo-actualizar'),
    path('prestamos/<int:pk>/eliminar/', EliminarPrestamo.as_view(), name='prestamo-eliminar'),
    path('libros/<int:libro_id>/prestamos/', PrestamoList.as_view(), name='prestamos-por-libro'),
]