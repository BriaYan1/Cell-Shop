from django.shortcuts import render

# Create your views here.
def vista_inicio(request):
    return render(request, 'index.html')

def vista_carrito(request):
    return render(request, 'vista_carrito.html')

def vista_detalle_producto(request):
    return render(request, 'vista_detalle_producto.html')

def vista_procesar_compra(request):
    return render(request, 'vista_procesar_compra.html')
