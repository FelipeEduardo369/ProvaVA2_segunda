from rest_framework import generics
from .models import DetalheTurma
from .serializers import DetalheTurmaSerializer

class DetalheTurmaListCreateView(generics.ListCreateAPIView):
    queryset = DetalheTurma.objects.all()
    serializer_class = DetalheTurmaSerializer

class DetalheTurmaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DetalheTurma.objects.all()
    serializer_class = DetalheTurmaSerializer

# Create your views here.
