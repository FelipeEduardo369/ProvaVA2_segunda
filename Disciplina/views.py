from rest_framework import generics
from .models import Disciplina
from .serializers import DisciplinaSerializer

class DisciplinaListCreateView(generics.ListCreateAPIView):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer

class DisciplinaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer

# Create your views here.
