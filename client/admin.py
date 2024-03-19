from django.contrib import admin
from .models import Cliente, ClienteAdjudicado
import random

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'cedula', 'correo_electronico', 'telefono', 'nombre_empresa', 'rnc', 'direccion', 'fecha_registro', 'activo')
    search_fields = ('nombre', 'apellido', 'cedula', 'correo_electronico', 'telefono', 'nombre_empresa', 'rnc', 'direccion')
    list_filter = ('activo', 'fecha_registro')

@admin.register(ClienteAdjudicado)
class ClienteAdjudicadoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'adjudicado', 'cliente', 'rnc_cedula', 'telefono', 'correo')
    search_fields = ('codigo', 'adjudicado__nombre', 'cliente', 'rnc_cedula', 'telefono', 'correo')
    list_filter = ('adjudicado__nombre',)
    readonly_fields = ('codigo',)

    def save_model(self, request, obj, form, change):
        if not obj.codigo:
            while True:
                codigo = str(random.randint(100000, 999999))
                if not ClienteAdjudicado.objects.filter(codigo=codigo).exists():
                    obj.codigo = codigo
                    break
        super().save_model(request, obj, form, change)
