from django.urls import path
from . import views

urlpatterns = [
    path('', views.vista_procesar_compra, name = 'vista_procesar_compra'),
]
