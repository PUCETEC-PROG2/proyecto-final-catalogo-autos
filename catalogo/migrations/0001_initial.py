# Generated by Django 4.2 on 2024-08-14 21:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(choices=[('SUV', 'Sport Utility Vehicle'), ('SEDAN', 'Sedán'), ('HATCHBACK', 'Hatchback'), ('COUPE', 'Coupé'), ('CONVERTIBLE', 'Convertible'), ('PICKUP', 'Pickup'), ('MINIVAN', 'Minivan'), ('SPORT', 'Deportivo')], max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('apellido', models.CharField(max_length=150)),
                ('cedula', models.BigIntegerField(unique=True)),
                ('telefono', models.BigIntegerField()),
                ('correo', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ciudad', models.CharField(max_length=50)),
                ('fecha_compra', models.DateField()),
                ('precio_total', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='catalogo.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo_producto', models.CharField(max_length=100)),
                ('marca_producto', models.CharField(max_length=200)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cilindraje', models.DecimalField(decimal_places=2, max_digits=7)),
                ('equipo', models.CharField(max_length=100)),
                ('motor', models.CharField(max_length=100)),
                ('transmision', models.CharField(max_length=100)),
                ('año', models.PositiveIntegerField()),
                ('color', models.CharField(max_length=300)),
                ('placa', models.CharField(max_length=20, unique=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='catalogo.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='LineaCompra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField(default=1)),
                ('compra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lineas', to='catalogo.compra')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogo.producto')),
            ],
        ),
        migrations.AddField(
            model_name='compra',
            name='productos',
            field=models.ManyToManyField(through='catalogo.LineaCompra', to='catalogo.producto'),
        ),
    ]
