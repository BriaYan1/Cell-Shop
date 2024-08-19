from django.shortcuts import render
from .models import *

# Create your views here.
def vista_inicio(request):
    productos = producto.objects.all()
    return render(request, 'index.html', {'producto': productos})

def vista_carrito(request):
    return render(request, 'vista_carrito.html')

def vista_detalle_producto(request):
    return render(request, 'vista_detalle_producto.html')

def vista_procesar_compra(request):
    return render(request, 'vista_procesar_compra.html')
