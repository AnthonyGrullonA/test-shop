# Generated by Django 5.0.3 on 2024-03-19 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0003_remove_clienteadjudicado_direccion_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='logo',
            field=models.ImageField(blank=True, default='', null=True, upload_to='logo/'),
        ),
    ]
