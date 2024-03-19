from django.db import models
import random

class Cliente(models.Model):
    # Información básica del cliente
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    cedula = models.CharField(max_length=11, unique=True)
    correo_electronico = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15)
    nombre_empresa = models.CharField(max_length=100, blank=True, null=True)
    rnc = models.CharField(max_length=9, blank=True, null=True)
    direccion = models.TextField()
    fecha_registro = models.DateField(auto_now_add=True)
    activo = models.BooleanField(default=True)
    logo = models.ImageField(upload_to='logo/', null=True, blank=True, default="")

    def __str__(self):
        return f" {self.nombre_empresa} | {self.nombre} {self.apellido} - {self.cedula}"

class ClienteAdjudicado(models.Model):
    adjudicado = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='clientes_adjudicados')
    codigo = models.CharField(max_length=10, unique=True, blank=True)
    cliente = models.CharField(max_length=100)
    rnc_cedula = models.CharField(max_length=11)
    telefono = models.CharField(max_length=15)
    correo = models.EmailField()

    def save(self, *args, **kwargs):
        if not self.codigo:
            while True:
                codigo = str(random.randint(100000, 999999))  # Genera un número aleatorio de 6 dígitos
                if not ClienteAdjudicado.objects.filter(codigo=codigo).exists():
                    self.codigo = codigo
                    break
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.codigo} | {self.cliente}"