
from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=60, null=False)
    apellido = models.CharField(max_length=150, null=False)
    cedula = models.BigIntegerField(null=False)
    telefono = models.BigIntegerField(null=False)
    correo = models.EmailField(null=False)

    def __str__(self) -> str:
        return f'{self.apellido} {self.nombre}'

class Categoria(models.Model):
    nombre_categoria = models.CharField(max_length=100, null=False)

    def __str__(self) -> str:
        return self.nombre_categoria

class Producto(models.Model):
    marca_producto = models.CharField(max_length=200, null=False)
    precio = models.DecimalField(null=False, max_digits=7, decimal_places=2)
    cilindraje = models.DecimalField(null=False, max_digits=7, decimal_places=2)
    equipo = models.CharField(max_length=100, null=False)
    motor = models.CharField(max_length=100, null=False)
    trasmision = models.TextField(max_length=200, null=False)
    año = models.DateField(null=False)
    color = models.TextField(max_length=300, null=False)
    pasajeros = models.IntegerField(null=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.RESTRICT)

    def __str__(self) -> str:
        return self.nombre_producto

class Compra(models.Model):
    ciudad = models.CharField(max_length=50, null=False)
    fecha_compra = models.DateField(null=False)
    precio_total = models.DecimalField(null=False, max_digits=10, decimal_places=2)
    cantidad = models.IntegerField(default=1, null=False)
    cliente = models.ForeignKey(Cliente, on_delete=models.RESTRICT)
    productos = models.ManyToManyField(Producto)

    def __str__(self) -> str:
        return f'Compra de {self.cliente} - {self.fecha_compra}'
