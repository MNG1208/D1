from django.urls import path
from .views import (
    ProductoListView,
    ProductoDetailView,
    ProductoCreateView,
    ProductoUpdateView,
    ProductoDeleteView
)

urlpatterns = [
    path('', ProductoListView.as_view(), name='producto-list'),
    path('<int:pk>/', ProductoDetailView.as_view(), name='producto-detail'),
    path('create/', ProductoCreateView.as_view(), name='producto-create'),
    path('<int:pk>/update/', ProductoUpdateView.as_view(), name='producto-update'),
    path('<int:pk>/delete/', ProductoDeleteView.as_view(), name='producto-delete'),
]
