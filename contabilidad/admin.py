# contabilidad/admin.py

from django.contrib import admin
from .models import CategoriaContable, CuentaContable, Transaccion, Balance

class CategoriaContableAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre', 'descripcion')

class CuentaContableAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'cliente', 'categoria', 'es_activo')
    list_filter = ('es_activo', 'categoria', 'cliente')
    search_fields = ('codigo', 'nombre', 'cliente__nombre')
    raw_id_fields = ('cliente', 'categoria', 'padre')

class TransaccionAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'cuenta', 'descripcion', 'monto', 'es_debito')
    list_filter = ('es_debito', 'cuenta', 'fecha')
    search_fields = ('cuenta__nombre', 'descripcion')
    date_hierarchy = 'fecha'
    raw_id_fields = ('cuenta',)

class BalanceAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'cuenta', 'saldo')
    list_filter = ('fecha', 'cuenta')
    search_fields = ('cuenta__nombre',)
    date_hierarchy = 'fecha'
    raw_id_fields = ('cuenta',)

admin.site.register(CategoriaContable, CategoriaContableAdmin)
admin.site.register(CuentaContable, CuentaContableAdmin)
admin.site.register(Transaccion, TransaccionAdmin)
admin.site.register(Balance, BalanceAdmin)
