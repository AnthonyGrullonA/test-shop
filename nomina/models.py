from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Empleado(models.Model):
    #usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    posicion = models.CharField(max_length=100)
    codigo_empleado = models.CharField(max_length=10, unique=True)
    salario_base = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"({self.codigo_empleado} - {self.nombre} {self.apellido})"

class RegistroPago(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, related_name='pagos')
    fecha_pago = models.DateField()
    monto_pago = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Pago a {self.empleado} - {self.fecha_pago}"
