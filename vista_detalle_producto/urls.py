from django.urls import path
from . import views

urlpatterns = [
    path('', views.vista_detalle_producto, name = 'vista_detalle_producto'),
]
