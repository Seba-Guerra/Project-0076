# Generated by Django 4.0.5 on 2024-12-08 21:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vehiculo',
            options={'permissions': [('visualizar_catalogo', 'Puede visualizar el catálogo de vehículos')]},
        ),
    ]
