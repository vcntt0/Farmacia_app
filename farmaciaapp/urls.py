from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('inventario/', views.listar_medicamentos, name='listar_medicamentos'),
    path('nuevo/', views.crear_medicamento, name='crear_medicamento'),
    path('editar/<int:pk>/', views.editar_medicamento, name='editar_medicamento'),
    path('eliminar/<int:pk>/', views.eliminar_medicamento, name='eliminar_medicamento'),
]