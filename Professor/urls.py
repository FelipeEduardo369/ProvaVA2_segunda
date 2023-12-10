from django.urls import path
from .views import ProfessorListCreateView, ProfessorDetailView

urlpatterns = [
    path('professor/', ProfessorListCreateView.as_view(), name='professor-list-create'),
    path('professor/<int:pk>/', ProfessorDetailView.as_view(), name='professor-detail'),
]