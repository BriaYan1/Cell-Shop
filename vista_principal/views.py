from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json

# Create your views here.
def vista_inicio(request):
    productos = Producto.objects.all()
    return render(request, 'index.html', {'producto': productos})

def vista_carrito(request):
    # Asumiendo que hay un usuario autenticado
    cliente = request.user.cliente
    orden, created = Orden.objects.get_or_create(cliente=cliente, completado=False)
    items = orden.order_items.all()

    total_carrito = sum([item.get_total for item in items])

    return render(request, 'vista_carrito.html', {'items': items, 'orden': orden, 'total_carrito': total_carrito,})

def vista_detalle_producto(request):
    return render(request, 'vista_detalle_producto.html')

def vista_procesar_compra(request):

    cliente = request.user.cliente
    orden, created = Orden.objects.get_or_create(cliente=cliente, completado=False)
    items = orden.order_items.all()

    total_carrito = sum([item.get_total for item in items])

    return render(request, 'vista_procesar_compra.html', {'items': items, 'orden': orden, 'total_carrito': total_carrito,})

def updateItem(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        productId = data.get('productId')
        action = data.get('action')

        # Validar que se recibieron productId y action
        if not productId or not action:
            return JsonResponse({'error': 'Faltan datos'}, status=400)

        try:
            product = Producto.objects.get(id=productId)
        except Producto.DoesNotExist:
            return JsonResponse({'error': 'Producto no encontrado'}, status=404)

        cliente = request.user.cliente
        orden, created = Orden.objects.get_or_create(cliente=cliente, completado=False)
        orden_item, created = OrdenItems.objects.get_or_create(orden=orden, producto=product)

        if action == 'add':
            orden_item.cantidad += 1
        elif action == 'remove':
            orden_item.cantidad -= 1

        # Evitar cantidades negativas
        if orden_item.cantidad < 0:
            orden_item.cantidad = 0

        orden_item.save()

        # Eliminar el item si la cantidad es 0
        if orden_item.cantidad == 0:
            orden_item.delete()

        return JsonResponse({'message': 'Producto actualizado', 'cantidad': orden_item.cantidad}, safe=False)

    return JsonResponse({'error': 'Método no permitido'}, status=405)
    
