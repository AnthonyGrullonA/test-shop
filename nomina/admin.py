from django.contrib import admin
from .models import Empleado, RegistroPago

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'posicion', 'codigo_empleado', 'salario_base')
    search_fields = ('nombre', 'apellido', 'codigo_empleado')
    ordering = ('codigo_empleado',)

@admin.register(RegistroPago)
class RegistroPagoAdmin(admin.ModelAdmin):
    list_display = ('empleado', 'fecha_pago', 'monto_pago')
    search_fields = ('empleado__nombre', 'empleado__apellido', 'empleado__codigo_empleado')
    ordering = ('-fecha_pago',)
