from django.urls import path
from .views import CursoListCreateView, CursoDetailView

urlpatterns = [
    path('curso/', CursoListCreateView.as_view(), name='curso-list-create'),
    path('curso/<int:pk>/', CursoDetailView.as_view(), name='curso-detail'),
]