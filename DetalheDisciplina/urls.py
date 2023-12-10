from django.urls import path
from .views import DetalheDisciplinaListCreateView, DetalheDisciplinaDetailView

urlpatterns = [
    path('detalhedisciplina/', DetalheDisciplinaListCreateView.as_view(), name='detalhedisciplina-list-create'),
    path('detalhedisciplina/<int:pk>/', DetalheDisciplinaDetailView.as_view(), name='detalhedisciplina-detail'),
]