from django.urls import path
from . import views
from .views import vista_procesar_compra

urlpatterns = [
    path('', views.vista_inicio, name = 'vista_inicio'),
    path('carrito/', views.vista_carrito, name = 'vista_carrito'),
    path('detalle/', views.vista_detalle_producto, name = 'vista_detalle_producto'),
    path('compra/', views.vista_procesar_compra, name = 'vista_procesar_compra'),
    path('procesar-compra/', vista_procesar_compra, name='procesar_compra'),
    path('update_item/', views.updateItem, name="comprar"),
]