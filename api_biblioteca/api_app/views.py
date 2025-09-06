from django.shortcuts import get_object_or_404, render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Autor, Editorial, Libro, Miembro
from .serializers import AutorSerializer, EditorialSerializer, LibroSerializer, MiembroSerializer

class AutorList(generics.ListCreateAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    
    def get(self, request):
        autores = self.get_queryset()
        serializer = AutorSerializer(autores, many=True)
        if not autores:
            raise NotFound("No se encontraron autores.")
        return Response({'success': True, 'detail': 'Listado de autores.', 'data': serializer.data}, status=status.HTTP_200_OK)
    
class CrearAutor(generics.CreateAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

    def post(self, request):
        serializer = AutorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'success': True, 'detail': 'Autor creado correctamente.', 'data': serializer.data}, status=status.HTTP_201_CREATED)
    
class ActualizarAutor(generics.UpdateAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

    def put(self, request, pk):
        autor = get_object_or_404(Autor, pk=pk)
        serializer = AutorSerializer(autor, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'success': True, 'detail': 'Autor actualizado correctamente.', 'data': serializer.data}, status=status.HTTP_200_OK)
    
class EliminarAutor(generics.DestroyAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

    def delete(self, request, pk):
        autor = get_object_or_404(Autor, pk=pk)
        autor.delete()
        return Response({'success': True, 'detail': 'Autor eliminado correctamente.'}, status=status.HTTP_204_NO_CONTENT)
    
class EditorialList(generics.ListCreateAPIView):
    queryset = Editorial.objects.all()
    serializer_class = EditorialSerializer

    def get(self, request):
        editoriales = self.get_queryset()
        serializer = EditorialSerializer(editoriales, many=True)
        if not editoriales:
            raise NotFound("No se encontraron editoriales.")
        return Response({'success': True, 'detail': 'Listado de editoriales.', 'data': serializer.data}, status=status.HTTP_200_OK)
    
class CrearEditorial(generics.CreateAPIView):
    queryset = Editorial.objects.all()
    serializer_class = EditorialSerializer

    def post(self, request):
        serializer = EditorialSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'success': True, 'detail': 'Editorial creada correctamente.', 'data': serializer.data}, status=status.HTTP_201_CREATED)
    
class ActualizarEditorial(generics.UpdateAPIView):
    queryset = Editorial.objects.all()
    serializer_class = EditorialSerializer

    def put(self, request, pk):
        editorial = get_object_or_404(Editorial, pk=pk)
        serializer = EditorialSerializer(editorial, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'success': True, 'detail': 'Editorial actualizada correctamente.', 'data': serializer.data}, status=status.HTTP_200_OK)
    
class EliminarEditorial(generics.DestroyAPIView):
    queryset = Editorial.objects.all()
    serializer_class = EditorialSerializer

    def delete(self, request, pk):
        editorial = get_object_or_404(Editorial, pk=pk)
        editorial.delete()
        return Response({'success': True, 'detail': 'Editorial eliminada correctamente.'}, status=status.HTTP_204_NO_CONTENT)
    
class LibroList(generics.ListCreateAPIView):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

    def get(self, request):
        libros = self.get_queryset()
        serializer = LibroSerializer(libros, many=True)
        if not libros:
            raise NotFound("No se encontraron libros.")
        return Response({'success': True, 'detail': 'Listado de libros.', 'data': serializer.data}, status=status.HTTP_200_OK)
    
class CrearLibro(generics.CreateAPIView):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

    def post(self, request):
        serializer = LibroSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'success': True, 'detail': 'Libro creado correctamente.', 'data': serializer.data}, status=status.HTTP_201_CREATED)
    
class ActualizarLibro(generics.UpdateAPIView):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

    def put(self, request, pk):
        libro = get_object_or_404(Libro, pk=pk)
        serializer = LibroSerializer(libro, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'success': True, 'detail': 'Libro actualizado correctamente.', 'data': serializer.data}, status=status.HTTP_200_OK)
    
class EliminarLibro(generics.DestroyAPIView):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

    def delete(self, request, pk):
        libro = get_object_or_404(Libro, pk=pk)
        libro.delete()
        return Response({'success': True, 'detail': 'Libro eliminado correctamente.'}, status=status.HTTP_204_NO_CONTENT)
    
class LibroFiltro(generics.ListCreateAPIView):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

    def get(self, request, *args, **kwargs):
        autor_id = kwargs.get('autor_id')
        editorial_id = kwargs.get('editorial_id')
        libros = self.get_queryset()
        if autor_id:
            libros = libros.filter(autor_id=autor_id)
        if editorial_id:
            libros = libros.filter(editorial_id=editorial_id)
        serializer = LibroSerializer(libros, many=True)
        if not libros:
            return Response({'success': False, 'detail': 'No se encontraron libros con los filtros proporcionados.'}, status=status.HTTP_404_NOT_FOUND)
        return Response({'success': True, 'detail': 'Listado de libros filtrados.', 'data': serializer.data}, status=status.HTTP_200_OK)

# miembros crud create, read, update, delete
class MiembroList(generics.ListCreateAPIView):
    queryset = Miembro.objects.all()
    serializer_class = MiembroSerializer

    def get(self, request):
        miembros = self.get_queryset()
        serializer = MiembroSerializer(miembros, many=True)
        if not miembros:
            raise NotFound("No se encontraron miembros.")
        return Response({'success': True, 'detail': 'Listado de miembros.', 'data': serializer.data}, status=status.HTTP_200_OK)


class CrearMiembro(generics.CreateAPIView):
    queryset = Miembro.objects.all()
    serializer_class = MiembroSerializer

    def post(self, request):
        serializer = MiembroSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'success': True, 'detail': 'Miembro creado correctamente.', 'data': serializer.data}, status=status.HTTP_201_CREATED)


class ActualizarMiembro(generics.UpdateAPIView):
    queryset = Miembro.objects.all()
    serializer_class = MiembroSerializer

    def put(self, request, pk):
        miembro = get_object_or_404(Miembro, pk=pk)
        serializer = MiembroSerializer(miembro, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'success': True, 'detail': 'Miembro actualizado correctamente.', 'data': serializer.data}, status=status.HTTP_200_OK)


class EliminarMiembro(generics.DestroyAPIView):
    queryset = Miembro.objects.all()
    serializer_class = MiembroSerializer

    def delete(self, request, pk):
        miembro = get_object_or_404(Miembro, pk=pk)
        miembro.delete()
        return Response({'success': True, 'detail': 'Miembro eliminado correctamente.'}, status=status.HTTP_204_NO_CONTENT)
# prestamos crud create, read, update, delete

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from django.shortcuts import get_object_or_404
from .models import Prestamo
from .serializers import PrestamoSerializer

class PrestamoList(generics.ListCreateAPIView):
    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer

    def get(self, request, miembro_id=None, libro_id=None):
        # Si la URL tiene miembro_id, filtramos por miembro
        if miembro_id:
            prestamos = Prestamo.objects.filter(miembro_id=miembro_id)
        # Si la URL tiene libro_id, filtramos por libro
        elif libro_id:
            prestamos = Prestamo.objects.filter(libro_id=libro_id)
        else:
            prestamos = self.get_queryset()

        if not prestamos.exists():
            raise NotFound("No se encontraron préstamos.")

        serializer = PrestamoSerializer(prestamos, many=True)
        return Response(
            {'success': True, 'detail': 'Listado de préstamos.', 'data': serializer.data},
            status=status.HTTP_200_OK
        )


class CrearPrestamo(generics.CreateAPIView):
    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer

    def post(self, request):
        serializer = PrestamoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {'success': True, 'detail': 'Préstamo creado correctamente.', 'data': serializer.data},
            status=status.HTTP_201_CREATED
        )


class ActualizarPrestamo(generics.UpdateAPIView):
    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer

    def put(self, request, pk):
        prestamo = get_object_or_404(Prestamo, pk=pk)
        serializer = PrestamoSerializer(prestamo, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {'success': True, 'detail': 'Préstamo actualizado correctamente.', 'data': serializer.data},
            status=status.HTTP_200_OK
        )


class EliminarPrestamo(generics.DestroyAPIView):
    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer

    def delete(self, request, pk):
        prestamo = get_object_or_404(Prestamo, pk=pk)
        prestamo.delete()
        return Response(
            {'success': True, 'detail': 'Préstamo eliminado correctamente.'},
            status=status.HTTP_204_NO_CONTENT
        )
