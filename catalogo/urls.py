from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


app_name= 'catalogo'

urlpatterns = [
    path("", views.index, name="index"),

    path("producto/", views.producto, name="producto"),    
    path('add_producto/', views.add_producto, name='add_producto'),    
    path("producto/edit_producto/<int:id>/", views.edit_producto, name="edit_producto"),
    path("producto/delete_producto/<int:id>/", views.delete_producto, name="delete_producto"),


    path("compra/", views.compra, name="compra"),    
    path('add_compra/', views.add_compra, name='add_compra'),

    path("cliente/", views.cliente, name="cliente"),
    path('add_cliente/', views.add_cliente, name='add_cliente'),
    path("cliente/edit_cliente/<int:id>/", views.edit_cliente, name="edit_cliente"),
    path("cliente/delete_cliente/<int:id>/", views.delete_cliente, name="delete_cliente"),


    path("categoria/", views.categoria, name="categoria"),
    path('add_categoria/', views.add_categoria, name='add_categoria'),

    path("login/", views.CustomLoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name='logout'),
]