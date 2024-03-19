# contabilidad/models.py

from django.db import models
from client.models import Cliente

class CategoriaContable(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class CuentaContable(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='cuentas_contables')
    categoria = models.ForeignKey(CategoriaContable, on_delete=models.PROTECT, related_name='cuentas')
    codigo = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    es_activo = models.BooleanField(default=True)
    padre = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='subcuentas')

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"

class Transaccion(models.Model):
    cuenta = models.ForeignKey(CuentaContable, on_delete=models.CASCADE, related_name='transacciones')
    fecha = models.DateTimeField()
    descripcion = models.TextField()
    monto = models.DecimalField(max_digits=12, decimal_places=2)
    es_debito = models.BooleanField(default=True)

    def __str__(self):
        tipo = "Débito" if self.es_debito else "Crédito"
        return f"{self.fecha.strftime('%Y-%m-%d %H:%M')} | {tipo} | {self.monto} | {self.cuenta.nombre}"

class Balance(models.Model):
    cuenta = models.ForeignKey(CuentaContable, on_delete=models.CASCADE, related_name='balances')
    fecha = models.DateField()
    saldo = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"{self.fecha} | Saldo: {self.saldo} | {self.cuenta.nombre}"
