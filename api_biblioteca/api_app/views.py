from django.shortcuts import get_object_or_404, render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Autor
from .serializers import AutorSerializer

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