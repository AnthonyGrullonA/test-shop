# Generated by Django 5.0.3 on 2024-03-19 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0002_alter_categoriaproducto_cliente_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='precio_compra',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=100),
        ),
        migrations.AlterField(
            model_name='producto',
            name='precio_venta',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=100),
        ),
    ]