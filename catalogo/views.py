from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from .forms import *
from .models import *


def index(request):

    return render(request, 'index.html')


def producto(request):

    productos = Producto.objects.order_by('categoria')

    context = {'productos': productos}

    return render(request, 'producto.html', context)


@login_required

def add_producto(request):

    if request.method == 'POST':

        form = ProductoForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('catalogo:producto')

    else:

        form = ProductoForm()

    return render(request, 'producto_form.html', {'form': form})


@login_required

def edit_producto(request, id):

    producto = get_object_or_404(Producto, pk=id)

    if request.method == 'POST':

        form = ProductoForm(request.POST, instance=producto)

        if form.is_valid():

            form.save()

            return redirect('catalogo:producto')

    else:

        form = ProductoForm(instance=producto)

    return render(request, 'producto_form.html', {'form': form})


@login_required

def delete_producto(request, id):

    producto = get_object_or_404(Producto, pk=id)

    producto.delete()

    return redirect('catalogo:producto')


def compra(request):

    compras = Compra.objects.order_by('fecha_compra')

    context = {'compras': compras}

    return render(request, 'compra.html', context)


@login_required

@login_required
def add_compra(request):
    if request.method == 'POST':
        form = CompraForm(request.POST)
        if form.is_valid():
            compra = form.save(commit=False)  # No guardamos la compra todavía
            productos = request.POST.getlist('productos')  # Obtener la lista de productos seleccionados
            for producto_id in productos:
                producto = Producto.objects.get(id=producto_id)
                LineaCompra.objects.create(compra=compra, producto=producto)
            compra.save()  # Ahora sí guardamos la compra
            return redirect('catalogo:compra')
    else:
        form = CompraForm()
    return render(request, 'compra_form.html', {'form': form})

def cliente(request):

    clientes = Cliente.objects.all()

    context = {'clientes': clientes}

    return render(request, 'cliente.html', context)


@login_required

def add_cliente(request):

    if request.method == 'POST':

        form = ClienteForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('catalogo:cliente')

    else:

        form = ClienteForm()

    return render(request, 'cliente_form.html', {'form': form})


@login_required

def edit_cliente(request, id):

    cliente = get_object_or_404(Cliente, pk=id)

    if request.method == 'POST':

        form = ClienteForm(request.POST, instance=cliente)

        if form.is_valid():

            form.save()

            return redirect('catalogo:cliente')

    else:

        form = ClienteForm(instance=cliente)

    return render(request, 'cliente_form.html', {'form': form})


@login_required

def delete_cliente(request, id):

    cliente = get_object_or_404(Cliente, pk=id)

    cliente.delete()

    return redirect('catalogo:cliente')


def categoria(request):

    categorias = Categoria.objects.all()

    context = {'categorias': categorias}

    return render(request, 'categoria.html', context)

@login_required
def delete_categoria(request, id):

    categoria = get_object_or_404(Categoria, pk=id)

    categoria.delete()

    return redirect('catalogo:categoria')


@login_required

def add_categoria(request):

    if request.method == 'POST':

        form = CategoriaForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('catalogo:categoria')

    else:

        form = CategoriaForm()

    return render(request, 'categoria_form.html', {'form': form})


class CustomLoginView(LoginView):
    template_name="login.html"
       