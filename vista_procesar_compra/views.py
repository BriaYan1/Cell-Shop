from django.shortcuts import render

# Create your views here.

def vista_procesar_compra(request):
    return render (request, 'vista_procesar_compra.html')