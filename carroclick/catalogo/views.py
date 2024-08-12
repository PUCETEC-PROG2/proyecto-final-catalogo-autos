
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template import loader
from .forms import *
from .models import *
from django.shortcuts import redirect, render
# #importacion de librearia de autenticacion 
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



#@login_required    
def add_producto(request):
    if request.method=='POST':
        form= ProductoForm(request.POST ,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('catalogo:index')
        
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

def compra(request):
    compra = Compra.objects.order_by('fecha_compra')
 
    context = {
        'compra' : compra
    }
    return render(request, 'compra.html', context)

#@login_required    
def add_compra(request):
    if request.method=='POST':
        form= CompraForm(request.POST ,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('catalogo:compra')
        
    else:   
        form = ProductoForm()
        
    return render(request,"compra_form.html",{'form': form }) 


def cliente (request):
    cliente = Cliente.objects.all()
    context = {
        'cliente' : cliente 
    }
    return render(request,'cliente.html', context )

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
    cliente = get_object_or_404(Producto, pk = id)
    if request.method == 'POST':
        form = ClienteForm(request.POST, request.FILES, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('catalogo:cliente')
    else:
        form = ClienteForm(instance=cliente)
    
    return render(request, 'cliente_form.html', {'form': form})

def delete_cliente(required, id):
    cliente = get_object_or_404(Producto, pk = id)
    cliente.delete()
    return redirect('catalogo:cliente')




class CustomLoginView(LoginView):
   template_name="login.html"
       

