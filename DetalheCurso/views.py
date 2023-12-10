from rest_framework import generics
from .models import DetalheCurso
from .serializers import DetalheCursoSerializer

class DetalheCursoListCreateView(generics.ListCreateAPIView):
    queryset = DetalheCurso.objects.all()
    serializer_class = DetalheCursoSerializer

class DetalheCursoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DetalheCurso.objects.all()
    serializer_class = DetalheCursoSerializer

# Create your views here.
