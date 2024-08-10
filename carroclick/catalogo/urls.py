from django.urls import path
from . import views


app_name= 'catalogo'

urlpatterns = [
    path("", views.index, name="index"),

    path("login/", views.CustomLoginView.as_view(), name="login"),

    path("cliente/", views.cliente, name="cliente"),
    path("cliente/add_cliente/<int:id>/", views.add_cliente, name="add_cliente"),
    path("cliente/edit_cliente/<int:id>/", views.edit_cliente, name="edit_cliente"),
    path("cliente/delete_cliente/<int:id>/", views.delete_cliente, name="delete_cliente"),

    
    path("producto/", views.producto, name="producto"),
    path("producto/add_producto/", views.add_producto, name="add_producto"),
    path("producto/edit_producto/<int:id>/", views.edit_producto, name="edit_producto"),
    path("producto/delete_producto/<int:id>/", views.delete_producto, name="delete_producto"),

    path("compra/", views.compra, name="compra"),
    path("compra/add_compra/", views.add_compra, name="add_compra"),
    
    
    
]

