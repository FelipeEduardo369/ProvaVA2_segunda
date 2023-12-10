from django.urls import path
from .views import DetalheTurmaListCreateView, DetalheTurmaDetailView

urlpatterns = [
    path('detalheturma/', DetalheTurmaListCreateView.as_view(), name='detalheturma-list-create'),
    path('detalheturma/<int:pk>/', DetalheTurmaDetailView.as_view(), name='detalheturma-detail'),
]