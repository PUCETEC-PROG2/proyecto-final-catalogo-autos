# Generated by Django 4.2 on 2024-08-15 02:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='compra',
            old_name='precio_total',
            new_name='precio',
        ),
    ]
