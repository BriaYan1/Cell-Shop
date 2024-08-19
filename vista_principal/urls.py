from django.urls import path
from . import views

urlpatterns = [
    path('', views.vista_inicio, name = 'vista_inicio'),
    path('carrito/', views.vista_carrito, name = 'vista_carrito'),
    path('detalle/', views.vista_detalle_producto, name = 'vista_detalle_producto')
]
