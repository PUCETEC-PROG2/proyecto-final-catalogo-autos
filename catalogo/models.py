from django.db import models
from django.forms import model_to_dict

class Cliente(models.Model):
    nombre = models.CharField(max_length=60, null=False)
    apellido = models.CharField(max_length=150, null=False)
    cedula = models.BigIntegerField(null=False, unique=True)
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
    categoria = models.CharField(max_length=30, choices=NOMBRE_CATEGORIA, null=False)

    def __str__(self) -> str:
        return self.categoria


class Producto(models.Model):
    modelo_producto = models.CharField(max_length=100, null=False)
    marca_producto = models.CharField(max_length=200, null=False)
    precio = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    cilindraje = models.DecimalField(max_digits=7, decimal_places=2, null=False)
    equipo = models.CharField(max_length=100, null=False)
    motor = models.CharField(max_length=100, null=False)
    transmision = models.CharField(max_length=100, null=False)
    año = models.PositiveIntegerField(null=False)
    color = models.CharField(max_length=300, null=False)
    placa = models.CharField(max_length=20, null=False, unique=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.RESTRICT)

    class Meta:
        verbose_name='producto'
        verbose_name_plural = 'productos'
        order_with_respect_to = 'año'
    
    def __str__(self):
        return self.modelo_producto
    
    def toJSON(self):
        item = model_to_dict(self, exclude=['año'])
        return item


class Compra(models.Model):

    cliente = models.ForeignKey(Cliente, on_delete=models.RESTRICT)
    productos = models.ManyToManyField(Producto, through='LineaCompra')
    ciudad = models.CharField(max_length=50, null=False)
    fecha_compra = models.DateField(null=False)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=False)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=False)
    
   

    def calculate_total(self):
        total = sum(item.Producto.precio for item in self.compraSUBTOTAL.all())
        self.total = total
        self.save()

    def __str__(self) -> str:
        return f'Compra de {self.cliente} - {self.fecha_compra}'


class LineaCompra(models.Model):
    compra = models.ForeignKey(Compra, related_name='lineas', on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.cantidad} x {self.producto.modelo_producto}"
