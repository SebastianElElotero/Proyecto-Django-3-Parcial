from django.urls import path
from . import views

urlpatterns = [
    path('panel/', views.panel_administracion, name='panel_administracion'),
    path('producto/editar/<int:producto_id>/', views.editar_producto, name='editar_producto'),
    path('producto/eliminar/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'),
]
