import datetime
from unittest import loader
from django.db import models
from django.forms import ValidationError
from django.http import HttpResponse

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=10)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nombre
    
class Categoria(models.Model):
    nombre = models.CharField(max_length=30, null=False)
    
    # categorías de tipo de auto
    AUTOS_TYPES = (
        ("S", "SEDAN"),
        ("H", "HATCHBACK"),
        ("C", "COUPE"),
        ("SUV", "SUV"),
        ("T", "TRUCK"),
        ("V", "VAN"),
        ("E", "ELECTRIC"),  
        ("C", "CONVERTIBLE"),  
        ("P", "PICKUP"),  
        # Puedes añadir más tipos según lo necesites.
    )

    type = models.CharField(max_length=30, choices=AUTOS_TYPES, null=False)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    anio = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='productos_images') 

    def clean(self):
        super().clean()  # Llama al método clean() de la superclase

        # Validar el año
        if self.anio < 1886 or self.anio > datetime.datetime.now().year:
            raise ValidationError('Año no válido.')


class Compra(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    fecha_compra = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Compra de {self.cliente} - {self.producto} el {self.fecha_compra}"
