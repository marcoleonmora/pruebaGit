from tkinter import CASCADE
from django.db import models

from accounts.models import Account

# Create your models here.

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    descripcion = models.CharField(max_length=300, null=True)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    unidad = models.CharField(max_length=10, null=False)
    imagen = models.ImageField(upload_to='productos')
    icono = models.ImageField(upload_to='iconos')
    

    def __str__(self):
        return self.nombre

class Carrito(models.Model):
    ESTADOS= (
        ('carrito', 'carrito'),
        ('cancelado', 'cancelado'),
        ('comprado', 'comprado'),
    )

    cliente=models.ForeignKey(Account, on_delete=models.CASCADE, null=False)
    producto=models.ForeignKey(Producto, on_delete=models.CASCADE, null=False)
    cantidad=models.IntegerField(default=1, null=False)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    estado=models.CharField(max_length=15, choices=ESTADOS, default='carrito')
    fecha=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.cliente) + ' - ' + str(self.producto)

    
    class Meta:
        verbose_name_plural = "Mi Carrito"
