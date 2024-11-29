from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import user_passes_test
from gestion_productos.models import Producto
from gestion_pedidos.models import Pedido
from gestion_pagos.models import Pago
from .forms import ProductoForm

# Verificación de rol de administrador
def es_administrador(user):
    return hasattr(user, 'administrador')

# Vista del panel de administración
def panel_administracion(request):
    productos = Producto.objects.all()
    pedidos = Pedido.objects.all()
    pagos = Pago.objects.all()
    return render(request, 'administracion/panel_administracion.html', {
        'productos': productos,
        'pedidos': pedidos,
        'pagos': pagos,
    })

# Vista para editar productos
#@user_passes_test(es_administrador)
def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('administracion:panel_administracion')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'administracion/editar_producto.html', {'form': form})

# Vista para eliminar productos
#@user_passes_test(es_administrador)
def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        producto.delete()
        return redirect('administracion:panel_administracion')
    return render(request, 'administracion/eliminar_producto.html', {'producto': producto})
