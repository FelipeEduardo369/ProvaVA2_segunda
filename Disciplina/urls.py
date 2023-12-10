from django.urls import path
from .views import DisciplinaListCreateView, DisciplinaDetailView

urlpatterns = [
    path('disciplina/', DisciplinaListCreateView.as_view(), name='disciplina-list-create'),
    path('disciplina/<int:pk>/', DisciplinaDetailView.as_view(), name='disciplina-detail'),
]