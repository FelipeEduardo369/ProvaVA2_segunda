from rest_framework import generics
from .models import Professor
from .serializers import ProfessorSerializer

class ProfessorListCreateView(generics.ListCreateAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer

class ProfessorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer

# Create your views here.
