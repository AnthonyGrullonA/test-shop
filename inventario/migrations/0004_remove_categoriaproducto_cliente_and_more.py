# Generated by Django 5.0.3 on 2024-03-19 02:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0003_alter_producto_precio_compra_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoriaproducto',
            name='cliente',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='cliente',
        ),
        migrations.RemoveField(
            model_name='proveedor',
            name='cliente',
        ),
    ]