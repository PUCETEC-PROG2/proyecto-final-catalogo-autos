from django import forms
from .models import *

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'cedula': forms.NumberInput(attrs={'class': 'form-control'}),
            'telefono': forms.NumberInput(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
        }

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'
        widgets = {
            'categoria': forms.Select(attrs={'class': 'form-control'}),
        }

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
        widgets = {
            'modelo_producto': forms.TextInput(attrs={'class': 'form-control'}),
            'marca_producto': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'cilindraje': forms.NumberInput(attrs={'class': 'form-control'}),
            'equipo': forms.TextInput(attrs={'class': 'form-control'}),
            'motor': forms.TextInput(attrs={'class': 'form-control'}),
            'transmision': forms.TextInput(attrs={'class': 'form-control'}),
            'año': forms.NumberInput(attrs={'class': 'form-control'}),
            'color': forms.TextInput(attrs={'class': 'form-control'}),
            'placa': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
        }

class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ['cliente', 'ciudad', 'fecha_compra', 'subtotal', 'total']
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-control'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_compra': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'subtotal': forms.NumberInput(attrs={'class': 'form-control'}),
            'total': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        productos = forms.ModelMultipleChoiceField(
            queryset=Producto.objects.all(),
            widget=forms.CheckboxSelectMultiple,
            required=False
        )

class LineaCompraForm(forms.ModelForm):
    class Meta:
        model = LineaCompra
        fields = ['producto', 'cantidad']
        widgets = {
            'producto': forms.Select(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
        }