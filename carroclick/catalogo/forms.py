from django import forms
from .models import Cliente, Categoria, Compra, Producto

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'  # Include all fields from the Cliente model
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'  # Include all fields from the Categoria model
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
        }


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'  # Include all fields from the Producto model
        widgets = {
            'marca': forms.TextInput(attrs={'class': 'form-control'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control'}),
            'anio': forms.NumberInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
        }


class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = '__all__'  # Include all fields from the Compra model
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-control'}),
            'producto': forms.Select(attrs={'class': 'form-control'}),
            # fecha_compra will be automatically added using auto_now_add
        }
