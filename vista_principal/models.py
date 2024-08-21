from django.db import models

# Create your models here.

class cliente(models.Model):
    nombre = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    telefono = models.IntegerField(null=False)
    direccion = models.CharField(max_length=500, null=False)

class producto(models.Model):
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

class orden(models.Model):
    fecha_orden = models.DateTimeField(auto_now_add= True)
    completado = models.BooleanField(default= False)
    id_transaccion = models.CharField(max_length= 100, null = True)

    def __str__(self):
        return str(self.id_transaccion)

class orden_items(models.Model):
    producto = models.ForeignKey(producto, on_delete=models.SET_NULL, null= True)
    orden = models.ForeignKey(orden, on_delete=models.SET_NULL, null= True)
    cantidad = models.IntegerField(default=0, null= True, blank= True)
    fecha = models.DateTimeField(auto_now_add=True)

class datos_envio(models.Model):
    cliente = models.ForeignKey(cliente, on_delete= models.SET_NULL, null= True)
    orden = models.ForeignKey(orden, on_delete= models.SET_NULL, null= True)
    fecha = models.DateTimeField(auto_now_add=True)
    direccion = models.CharField(max_length= 100, null = True)

    def __str__(self):
        return str(self.direccion)