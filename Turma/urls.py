from django.urls import path
from .views import TurmaListCreateView, TurmaDetailView

urlpatterns = [
    path('list_create/', TurmaListCreateView.as_view(), name='turma-list-create'),
    path('<int:pk>/', TurmaDetailView.as_view(), name='turma-detail'),
]