from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=60, null=False)
    apellido = models.CharField(max_length=150, null=False)
    cedula = models.BigIntegerField(null=False, unique=True)  # Añadido índice único
    telefono = models.BigIntegerField(null=False)
    correo = models.EmailField(null=False)

    def __str__(self) -> str:
        return f'{self.apellido} {self.nombre}'


class Categoria(models.Model):
    
    NOMBRE_CATEGORIA = [
    ('SUV', 'Sport Utility Vehicle'),
    ('SEDAN', 'Sedán'),
    ('HATCHBACK', 'Hatchback'),
    ('COUPE', 'Coupé'),
    ('CONVERTIBLE', 'Convertible'),
    ('PICKUP', 'Pickup'),
    ('MINIVAN', 'Minivan'),
    ('SPORT', 'Deportivo'),
]
    categoria = models.CharField(max_length=30, choices=NOMBRE_CATEGORIA, null=False, blank=False)    
    
    def __str__(self)-> str:
        return self.categoria



class Producto(models.Model):
    modelo_producto = models.CharField(max_length=100, null=False)  # Añadido el nombre del producto
    marca_producto = models.CharField(max_length=200, null=False)
    precio = models.DecimalField(null=False, max_digits=10, decimal_places=2)  # Aumenté max_digits
    cilindraje = models.DecimalField(null=False, max_digits=7, decimal_places=2)
    equipo = models.CharField(max_length=100, null=False)
    motor = models.CharField(max_length=100, null=False)
    trasmision = models.CharField(null=False)
    año = models.IntegerField(null=False)
    color = models.CharField(max_length=300, null=False)
    placa = models.CharField(null=False,unique=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.RESTRICT)

    def __str__(self) -> str:
        return self.modelo_producto

class Compra(models.Model):
    ciudad = models.CharField(max_length=50, null=False)
    fecha_compra = models.DateField(null=False)
    precio_total = models.DecimalField(null=False, max_digits=10, decimal_places=2)
    cantidad = models.IntegerField(default=1, null=False)
    cliente = models.ForeignKey(Cliente, on_delete=models.RESTRICT)
    productos = models.ManyToManyField(Producto)

    def __str__(self) -> str:
        return f'Compra de {self.cliente} - {self.fecha_compra}'
    
    
