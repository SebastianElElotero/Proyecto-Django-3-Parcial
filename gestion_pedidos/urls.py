from django.urls import path
from . import views

urlpatterns = [
    path('pedidos/', views.listar_pedidos, name='listar_pedidos'),
    path('pedidos/crear/', views.crear_pedido, name='crear_pedido'),
    path('pedidos/editar/<int:pedido_id>/', views.editar_pedido, name='editar_pedido'),
    path('pedidos/eliminar/<int:pedido_id>/', views.eliminar_pedido, name='eliminar_pedido'),
    path('pedidos/agregar_item/<int:pedido_id>/', views.agregar_item_pedido, name='agregar_item_pedido'),
]