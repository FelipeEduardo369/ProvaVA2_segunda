from django.urls import path
from .views import AlunoListCreateView,AlunoDetailView

urlpatterns = [
    path('aluno/', AlunoListCreateView.as_view(), name='aluno-list-create'),
    path('aluno/<int:pk>/', AlunoDetailView.as_view(), name='aluno-detail'),
]