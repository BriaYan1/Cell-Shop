import stripe
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from django.http import JsonResponse
from django.db import transaction
import json

# Create your views here.

def obtener_total_productos(cliente):
    orden, created = Orden.objects.get_or_create(cliente=cliente, completado=False)
    total_productos = sum([item.cantidad for item in orden.order_items.all()])
    return total_productos

def vista_inicio(request):
    productos = Producto.objects.all()

    if request.user.is_authenticated:
        cliente = request.user.cliente
        total_productos = obtener_total_productos(cliente)
    else:
        total_productos = 0  # o algún valor por defecto

    return render(request, 'index.html', {'producto': productos, 'total_productos': total_productos})



def vista_carrito(request):
    cliente = request.user.cliente
    orden, created = Orden.objects.get_or_create(cliente=cliente, completado=False)
    items = orden.order_items.all()
    total_carrito = sum([item.get_total for item in items])
    total_productos = obtener_total_productos(cliente)

    return render(request, 'vista_carrito.html', {
        'items': items,
        'orden': orden,
        'total_carrito': total_carrito,
        'total_productos': total_productos,
    })

def vista_detalle_producto(request):
    return render(request, 'vista_detalle_producto.html')

def vista_procesar_compra(request):
    cliente = request.user.cliente
    orden, created = Orden.objects.get_or_create(cliente=cliente, completado=False)

    items = orden.order_items.all()
    total_productos = obtener_total_productos(cliente)
    total_carrito = sum([item.get_total for item in items])

    if request.method == 'POST':
        # Aquí iría la lógica para procesar el pago (omitida por simplicidad)

        try:
            with transaction.atomic():
                # Marca la orden como completada
                orden.completado = True
                orden.save()

                # Eliminar los artículos del carrito
                orden.order_items.all().delete()  # Elimina todos los artículos de la orden

            return redirect('vista_inicio')

        except Exception as e:
            # Manejo de errores
            messages.error(request, "Error procesando la compra: {}".format(str(e)))
            return render(request, 'vista_procesar_compra.html', {
                'items': items,
                'orden': orden,
                'total_carrito': total_carrito,
                'total_productos': total_productos,
            })

    return render(request, 'vista_procesar_compra.html', {
        'items': items,
        'orden': orden,
        'total_carrito': total_carrito,
        'total_productos': total_productos,
    })

def updateItem(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        productId = data.get('productId')
        action = data.get('action')

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

        if orden_item.cantidad < 0:
            orden_item.cantidad = 0

        orden_item.save()

        if orden_item.cantidad == 0:
            orden_item.delete()

        total_productos = sum(item.cantidad for item in orden.order_items.all())
        return JsonResponse({'message': 'Producto actualizado', 'cantidad': orden_item.cantidad, 'total_productos': total_productos})

    return JsonResponse({'error': 'Método no permitido'}, status=405)