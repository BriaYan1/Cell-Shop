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
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action:', action)
    print('productId', productId)

    cliente = request.user.cliente
    product = Producto.objects.get(id=productId)
    orden, created = Orden.objects.get_or_create(cliente=cliente, completado=False)

    OrdenItems, created = OrdenItems.objects.get_or_create(orden=orden, product=product)

    if action == 'add':
        OrdenItems.cantidad = (OrdenItems.cantidad + 1)
    elif action == 'remove':
        OrdenItems.cantidad = (OrdenItems.cantidad - 1)

    OrdenItems.save()

    if OrdenItems.cantidad <= 0:
        OrdenItems.delete()
    
        
    return JsonResponse('El producto fue agregado', safe=False)