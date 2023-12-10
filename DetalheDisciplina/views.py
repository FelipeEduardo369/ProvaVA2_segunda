
from rest_framework import generics
from .models import DetalheDisciplina
from .serializers import DetalheDisciplinaSerializer

class DetalheDisciplinaListCreateView(generics.ListCreateAPIView):
    queryset = DetalheDisciplina.objects.all()
    serializer_class = DetalheDisciplinaSerializer

class DetalheDisciplinaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DetalheDisciplina.objects.all()
    serializer_class = DetalheDisciplinaSerializer

