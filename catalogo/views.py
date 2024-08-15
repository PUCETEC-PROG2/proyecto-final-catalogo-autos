
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template import loader
from .forms import *
from .models import *
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required

def index(request):

    template = loader.get_template('index.html')
    return HttpResponse(template.render({'index': index}, request))

def producto(request):
    producto = Producto.objects.order_by('categoria')
    context = {
        'producto' : producto
    }
    return render(request, 'producto.html', context)

def compra(request):
    compra = Compra.objects.order_by('fecha_compra')
     
    context = {
        'compra' : compra
    }
    return render(request, 'compra.html', context)


def cliente (request):
    cliente = Cliente.objects.all()
    context = {
        'cliente' : cliente 
    }
    return render(request,'cliente.html', context )

def categoria (request):
    categoria = Categoria.objects.all()
    context = {
        'categoria' : categoria 
    }
    return render(request,'categoria.html', context )




def add_categoria(request):
    if request.method=='POST':
        form= CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogo:categoria')
        
    else:   
        form = CategoriaForm()
        
    return render(request,"categoria_form.html",{'form': form }) 


#@login_required    
def add_producto(request):
    if request.method=='POST':
        form= ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogo:producto')
        
    else:   
        form = ProductoForm()
        
    return render(request,"producto_form.html",{'form': form }) 

def edit_producto(request, id):
    producto = get_object_or_404(Producto, pk = id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('catalogo:producto')
    else:
        form = ProductoForm(instance=producto)
    
    return render(request, 'producto_form.html', {'form': form})

def delete_producto(required, id):
    producto = get_object_or_404(Producto, pk = id)
    producto.delete()
    return redirect('catalogo:producto')



#@login_required   
def add_compra(request):
    if request.method == 'POST':
        form = CompraForm(request.POST)
        if form.is_valid():
            compra = form.save()  # Guarda la compra

            selected_productos = request.POST.getlist('producto')
            for producto_id in selected_productos:
                try:
                    producto = Producto.objects.get(id=producto_id)  # Obtiene el producto
                    LineaCompra.objects.create(compra=compra, producto=producto)  # Crea la Línea de Compra
                except Producto.DoesNotExist:
                    # Manejo de error en caso de que el producto no exista
                    # Puedes registrar un mensaje de error o simplemente continuar
                    pass

            return render(request, 'compra.html') # Redirige a una vista de éxito

    else:
        form = CompraForm()  # Si no es POST, crea un nuevo formulario

    return render(request, 'compra_form.html', {'form': form})  # Renderiza el formulario








def add_cliente(request):
    if request.method=='POST':
        form= ClienteForm(request.POST ,request.FILES) 
        if form.is_valid():
            form.save()
            return redirect('catalogo:cliente')
        
    else:   
        form = ClienteForm()
        
    return render(request,"cliente_form.html",{'form': form }) 

def edit_cliente(request, id):
    cliente = get_object_or_404(Cliente, pk = id)
    if request.method == 'POST':
        form = ClienteForm(request.POST, request.FILES, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('catalogo:cliente')
    else:
        form = ClienteForm(instance=cliente)
    
    return render(request, 'cliente_form.html', {'form': form})

def delete_cliente(required, id):
    cliente = get_object_or_404(Cliente, pk = id)
    cliente.delete()
    return redirect('catalogo:cliente')




class CustomLoginView(LoginView):
   template_name="login.html"
       

