# Generated by Django 5.0.3 on 2024-03-18 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_picture',
            field=models.ImageField(blank=True, default='', null=True, upload_to='profile_pictures/'),
        ),
    ]
