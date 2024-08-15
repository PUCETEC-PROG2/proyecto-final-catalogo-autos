from django.contrib import admin
from .models import Cliente, LineaCompra,Producto,Categoria,Compra

# Register your models here.
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    pass

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    pass

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    pass

@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    pass

@admin.register(LineaCompra)
class LineaCompraAdmin(admin.ModelAdmin):
    pass