from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Cliente(models.Model):
    usuario = models.OneToOneField(User, null=True,blank=True,on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    telefono = models.IntegerField(null=False)

class Producto(models.Model):
    nombre = models.CharField(max_length=200, null=True)
    precio = models.FloatField()
    ram = models.CharField(max_length=200, null=True)
    almacenamiento = models.CharField(max_length=200, null=True)
    cpu = models.CharField(max_length=200, null=True)
    camara_trasera = models.CharField(max_length=200, null=True)
    camara_frontal = models.CharField(max_length=200, null=True)
    pantalla = models.CharField(max_length=200, null=True)
    bateria = models.CharField(max_length=200, null=True)
    android = models.CharField(max_length=200, null=True)
    color = models.CharField(max_length=200, null=True)
    cantidad = models.IntegerField()
    imagen = models.ImageField(null=True, blank=True)

    def __str__(self):
        return str(self.nombre)

class Orden(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete= models.SET_NULL, null= True)
    fecha_orden = models.DateTimeField(auto_now_add= True)
    completado = models.BooleanField(default= False)
    id_transaccion = models.CharField(max_length= 100, null = True)

    def __str__(self):
        return str(self.id_transaccion)

class OrdenItems(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True)
    orden = models.ForeignKey(Orden, related_name='order_items', on_delete=models.SET_NULL, null=True)
    cantidad = models.IntegerField(default=0, null=True, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        return self.cantidad * self.producto.precio


class DatosEnvio(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete= models.SET_NULL, null= True)
    orden = models.ForeignKey(Orden, on_delete= models.SET_NULL, null= True)
    fecha = models.DateTimeField(auto_now_add=True)
    direccion = models.CharField(max_length= 100, null = True)

    def __str__(self):
        return str(self.direccion)