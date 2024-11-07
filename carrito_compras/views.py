from django.shortcuts import render, redirect, get_object_or_404
from .models import Carrito, ItemCarrito
from .forms import ItemCarritoForm
from gestion_productos.models import Producto


# Ver el carrito
def ver_carrito(request):
    carrito, created = Carrito.objects.get_or_create(usuario=request.user)
    return render(request, 'carrito_compras/ver_carrito.html', {'carrito': carrito})

# Agregar un producto al carrito
def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    carrito, created = Carrito.objects.get_or_create(usuario=request.user)
    item, created = ItemCarrito.objects.get_or_create(carrito=carrito, producto=producto)
    
    if request.method == 'POST':
        form = ItemCarritoForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('ver_carrito')
    else:
        form = ItemCarritoForm(instance=item)
    return render(request, 'carrito_compras/agregar_al_carrito.html', {'form': form, 'producto': producto})

# Actualizar la cantidad de un item en el carrito
def actualizar_item_carrito(request, item_id):
    item = get_object_or_404(ItemCarrito, id=item_id)
    if request.method == 'POST':
        form = ItemCarritoForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('ver_carrito')
    else:
        form = ItemCarritoForm(instance=item)
    return render(request, 'carrito_compras/actualizar_item_carrito.html', {'form': form})

# Eliminar un item del carrito
def eliminar_item_carrito(request, item_id):
    item = get_object_or_404(ItemCarrito, id=item_id)
    if request.method == 'POST':
        item.delete()
        return redirect('ver_carrito')
    return render(request, 'carrito_compras/eliminar_item_carrito.html', {'item': item})
