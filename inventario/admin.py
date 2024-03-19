from django.contrib import admin
from .models import CategoriaProducto, Proveedor, Producto
import uuid

@admin.register(CategoriaProducto)
class CategoriaProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre', 'descripcion')

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'telefono', 'direccion')
    search_fields = ('nombre', 'telefono', 'direccion')

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'descripcion', 'precio_compra', 'precio_venta', 'stock', 'codigo_barra', 'proveedor', 'fecha_gasto', 'total_gasto')
    search_fields = ('nombre', 'categoria__nombre', 'descripcion', 'precio_compra', 'precio_venta', 'stock', 'codigo_barra', 'proveedor__nombre')
    list_filter = ('categoria', 'proveedor')
    readonly_fields = ('codigo', 'codigo_barra', 'total_gasto', 'fecha_gasto')

    def save_model(self, request, obj, form, change):
        if not obj.codigo:
            obj.codigo = str(uuid.uuid4()).replace('-', '')[:6]
        if not obj.codigo_barra:
            obj.codigo_barra = str(uuid.uuid4()).replace('-', '')[:12]
        obj.total_gasto = obj.stock * obj.precio_compra
        super().save_model(request, obj, form, change)
