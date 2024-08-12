from django import forms
from .models import *

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
        widgets = {
           'marca_producto' : forms.TextInput(attrs={'class' : 'form-control'}),
           'precio' : forms.NumberInput(attrs={'class' : 'form-control'}),
           'cilindraje' : forms.NumberInput(attrs={'class' : 'form-control'}),
           'equipo' : forms.TextInput(attrs={'class' : 'form-control'}),
           'motor' : forms.Textarea(attrs={'class' : 'form-control'}),
           'trasmision' : forms.Textarea(attrs={'class' : 'form-control'}),
           'año' : forms.DateInput(attrs={'class' : 'form-control'}),
           'color' : forms.Textarea(attrs={'class' : 'form-control'}),
           'pasajeros' : forms.NumberInput(attrs={'class' : 'form-control'}),
           'categoria' : forms.Select(attrs={'class' : 'form-control'})
        }

class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = '__all__'
        widgets = {
           'ciudad' : forms.TextInput(attrs={'class' : 'form-control'}),
           'fecha_compra' : forms.DateInput(attrs={'class' : 'form-control'}),
           'precio_total' : forms.NumberInput(attrs={'class' : 'form-control'}),
           'cantidad' : forms.NumberInput(attrs={'class' : 'form-control'}),
           'cliente' : forms.Select(attrs={'class' : 'form-control'}),
           'productos' : forms.Select(attrs={'class' : 'form-control'}),
        }

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        widgets = {
           'nombre' : forms.TextInput(attrs={'class' : 'form-control'}),
           'apellido' : forms.TextInput(attrs={'class' : 'form-control'}),
           'edad' : forms.NumberInput(attrs={'class' : 'form-control'}),
           'cedula' : forms.NumberInput(attrs={'class' : 'form-control'}),
           'telefono' : forms.NumberInput(attrs={'class' : 'form-control'}),
           'correo' : forms.Textarea(attrs={'class' : 'form-control'}),
           
        }        