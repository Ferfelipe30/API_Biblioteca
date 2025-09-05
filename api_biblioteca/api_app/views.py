from django.shortcuts import get_object_or_404, render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Autor, Editorial
from .serializers import AutorSerializer, EditorialSerializer

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