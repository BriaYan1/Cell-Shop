from django.shortcuts import render

# Create your views here.

def vista_detalle_producto(request):
    return render (request, 'vista_detalle_producto.html')