from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(cliente)
admin.site.register(producto)
admin.site.register(orden)
admin.site.register(orden_items)
admin.site.register(datos_envio)