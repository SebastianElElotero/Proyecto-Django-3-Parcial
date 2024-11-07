from django.urls import path
from . import views
app_name = "gestion_productos"

urlpatterns = [
    # URLs de productos
    path('productos/', views.listar_productos, name='listar_productos'),
    path('productos/agregar/', views.agregar_producto, name='agregar_producto'),
    path('productos/editar/<int:producto_id>/', views.editar_producto, name='editar_producto'),
    path('productos/eliminar/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'),

    # URLs de categorías
    path('categorias/', views.listar_categorias, name='listar_categorias'),
    path('categorias/agregar/', views.agregar_categoria, name='agregar_categoria'),
]