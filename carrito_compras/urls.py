from django.urls import path
from . import views
app_name = "carrito_compras"

urlpatterns = [
    path('carrito/', views.ver_carrito, name='ver_carrito'),
    path('carrito/agregar/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/actualizar/<int:item_id>/', views.actualizar_item_carrito, name='actualizar_item_carrito'),
    path('carrito/eliminar/<int:item_id>/', views.eliminar_item_carrito, name='eliminar_item_carrito'),
]