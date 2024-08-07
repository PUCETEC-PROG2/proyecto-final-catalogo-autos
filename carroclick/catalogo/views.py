
from django.http import HttpResponse
from django.template import loader
from catalogo.forms import ProductoForm,CategoriaForm
from catalogo.forms import ClienteForm,CompraForm
from .models import Cliente,Producto,Categoria,Compra
from django.shortcuts import get_object_or_404, redirect, render

#importacion de librearia de autenticacion 
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required

def index(request):
    #pokemons = Pokemon.objects.all() ## SELECT * FROM pokedex_pokemon
    clientes = Cliente.objects.all() ## SELECT * FROM pokedex_pokemon ORD
    productos = Producto.objects.all()
    template = loader.get_template('index.html')
    
    return HttpResponse(template.render({'clientes': clientes, 'productos':productos}, request))
 
def cliente(request, cliente_id):
    
    cliente = get_object_or_404(Cliente,id=cliente_id)
    template = loader.get_template('display_cliente.html')
    context = {
        'cliente' : cliente
    }
    return HttpResponse(template.render(context, request))

def producto(request, producto_id):
    #SELECT * FROM pokedex_trainer WHERE id='trainer_id'
    proucto = get_object_or_404(Producto,id=producto_id)
    template = loader.get_template('display_producto.html')
    context = {
        'producto': producto
    }
    return HttpResponse(template.render(context, request))

def categoria(request, categoria_id):
   
    categoria = get_object_or_404(Categoria,id=categoria_id)
    template = loader.get_template('display_categoria.html')
    context = {
        'categoria': categoria
    }
    return HttpResponse(template.render(context, request))

def compra(request, compra_id):
   
    compra = get_object_or_404(Compra,id=compra_id)
    template = loader.get_template('display_compra.html')
    context = {
        'compra': compra
    }
    return HttpResponse(template.render(context, request))

@login_required    
def add_categoria(request):
    if request.method=='POST':
        form= CategoriaForm(request.POST ,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('catalogo:index')
        
    else:
    
        form = CategoriaForm()
        
    return render(request,"categoria_form.html",{'form': form }) 
@login_required    
def add_compra(request):
    if request.method=='POST':
        form= CompraForm(request.POST ,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('catalogo:index')
        
    else:
    
        form = CompraForm()
        
    return render(request,"compra_form.html",{'form': form }) 

@login_required 
def edit_compra(request,id):
    
    compra= get_object_or_404(Compra, pk =id)
    if request.method=='POST':
        form= CompraForm(request.POST ,request.FILES,instance=compra)
        if form.is_valid():
            form.save()
            return redirect('catalogo:index')
        
    else:
    
        form = CompraForm(instance=compra)
        
    return render(request,"compra_form.html",{'form': form }) 


@login_required    
def add_producto(request):
    if request.method=='POST':
        form= ProductoForm(request.POST ,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('catalogo:index')
        
    else:
    
        form = ProductoForm()
        
    return render(request,"producto_form.html",{'form': form }) 
@login_required 
def edit_producto(request,id):
    
    proucto= get_object_or_404(Producto, pk =id)
    if request.method=='POST':
        form= ProductoForm(request.POST ,request.FILES,instance=producto)
        if form.is_valid():
            form.save()
            return redirect('catalogo:index')
        
    else:
    
        form = ProductoForm(instance=producto)
        
    return render(request,"producto_form.html",{'form': form }) 

@login_required
def delete_producto(request,id):
    producto=get_object_or_404(Producto,pk=id)
    producto.delete()
    return redirect('catalogo:index')


@login_required    
def add_cliente(request):
    if request.method=='POST':
        form= ClienteForm(request.POST ,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('catalogo:index')
        
    else:
    
        form = ClienteForm()
        
    return render(request,"cliente_form.html",{'form': form }) 
@login_required 
def edit_cliente(request,id):
    
    cliente= get_object_or_404(Cliente, pk =id)
    if request.method=='POST':
        form= ClienteForm(request.POST ,request.FILES,instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('catalogo:index')
        
    else:
    
        form = ClienteForm(instance=cliente)
        
    return render(request,"cliente_form.html",{'form': form }) 

@login_required
def delete_cliente(request,id):
    cliente=get_object_or_404(Cliente,pk=id)
    cliente.delete()
    return redirect('catalogo:index')


class CustomLoginView(LoginView):
    template_name="login.html"
       
