from rest_framework import generics
from .models import Aluno
from .serializers import AlunoSerializer

class AlunoListCreateView(generics.ListCreateAPIView):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class AlunoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

# Create your views here.
