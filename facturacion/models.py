from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from client.models import ClienteAdjudicado as client
from inventario.models import Producto

class Factura(models.Model):
    cliente = models.ForeignKey(client, on_delete=models.CASCADE)
    fecha_emision = models.DateField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Factura {self.id}"

class ElementoFactura(models.Model):
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE, related_name='elementos')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def save(self, *args, **kwargs):
        self.precio_unitario = self.producto.precio_venta
        super().save(*args, **kwargs)

    def subtotal(self):
        return self.cantidad * self.precio_unitario

    def __str__(self):
        return f"Elemento {self.id} de {self.factura}"

# Señal para actualizar el total de la factura al guardar un elemento de factura
@receiver(post_save, sender=ElementoFactura)
def actualizar_total_factura(sender, instance, **kwargs):
    total = sum(elemento.subtotal() for elemento in instance.factura.elementos.all())
    instance.factura.total = total
    instance.factura.save()

# Señal para actualizar el costo total del producto al guardar un producto
@receiver(pre_save, sender=Producto)
def actualizar_costo_producto(sender, instance, **kwargs):
    instance.total_gasto = instance.precio_compra * instance.stock
