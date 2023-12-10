from rest_framework import generics
from .models import Turma
from .serializers import TurmaSerializer

class TurmaListCreateView(generics.ListCreateAPIView):
    queryset = Turma.objects.all()
    serializer_class = TurmaSerializer

class TurmaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Turma.objects.all()
    serializer_class = TurmaSerializer

# Create your views here.
