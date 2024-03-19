from django.db import models
import uuid
from django.utils import timezone

class CategoriaProducto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    direccion = models.TextField()


    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    codigo = models.CharField(max_length=100, unique=True, blank=True)
    nombre = models.CharField(max_length=200)
    categoria = models.ForeignKey(CategoriaProducto, on_delete=models.CASCADE, related_name='productos')
    descripcion = models.TextField(blank=True, null=True)
    precio_compra = models.DecimalField(max_digits=100, decimal_places=2, default=00.00)
    precio_venta = models.DecimalField(max_digits=100, decimal_places=2, default=00.00)
    stock = models.IntegerField(default=0)
    codigo_barra = models.CharField(max_length=15, blank=True, unique=True)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, related_name='productos_proveedor')
    fecha_gasto = models.DateField(default=timezone.now)
    total_gasto = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)


    def save(self, *args, **kwargs):
        if not self.codigo:
            self.codigo = str(uuid.uuid4()).replace('-', '')[:6]
        if not self.codigo_barra:
            self.codigo_barra = str(uuid.uuid4()).replace('-', '')[:12]
        self.total_gasto = self.precio_compra * self.stock
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nombre} ({self.codigo})"
