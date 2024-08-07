from django.urls import path
from . import views


app_name= 'catalogo'

urlpatterns = [
    path("", views.index, name="index"),

    path("login/", views.CustomLoginView.as_view(), name="login"),

    path("cliente/<int:cliente_id>/", views.cliente, name="cliente"),
    path("add_cliente/", views.add_cliente, name="add_cliente"),
    path("edit_cliente/<int:id>/", views.edit_cliente, name="edit_cliente"),
    path("delete_cliente/<int:id>/", views.delete_cliente, name="delete_cliente"),

    
    path("producto/<int:producto_id>/", views.producto, name="producto"),
    path("add_producto/", views.add_producto, name="add_producto"),
    path("edit_producto/<int:id>/", views.edit_producto, name="edit_producto"),
    path("delete_producto/<int:id>/", views.delete_producto, name="delete_producto"),

    path("compra/<int:compra_id>/", views.compra, name="compra"),
    path("add_compra/", views.add_compra, name="add_compra"),
    path("edit_compra/<int:id>/", views.edit_compra, name="edit_compra"),
    

    path("categoria/<int:categoria_id>/", views.categoria, name="categoria"),
     path("add_categoria/", views.add_categoria, name="add_categoria"),
    
]

