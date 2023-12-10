from django.urls import path
from .views import DetalheCursoListCreateView, DetalheCursoDetailView

urlpatterns = [
    path('detalhecurso/', DetalheCursoListCreateView.as_view(), name='detalhecurso-list-create'),
    path('detalhecurso/<int:pk>/', DetalheCursoDetailView.as_view(), name='detalhecurso-detail'),
]