from django.shortcuts import render

# Create your views here.
def vista_carrito(request):
    return render (request, 'vista_carrito.html')