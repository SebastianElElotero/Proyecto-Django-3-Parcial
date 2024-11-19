from django.shortcuts import render, get_object_or_404, redirect
from .models import Pedido, ItemPedido
from .forms import PedidoForm, ItemPedidoForm
from django.contrib.auth.models import User
from gestion_productos.models import Producto

# Listar pedidos
def listar_pedidos(request):
    pedidos = Pedido.objects.filter()
    return render(request, 'gestion_pedidos/listar_pedidos.html', {'pedidos': pedidos})

# Crear un nuevo pedido
def crear_pedido(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            pedido = form.save(commit=False)
            pedido.usuario = request.user
            pedido.save()
            return redirect('listar_pedidos')
    else:
        form = PedidoForm()
    return render(request, 'gestion_pedidos/crear_pedido.html', {'form': form})

# Editar un pedido existente
def editar_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    if request.method == 'POST':
        form = PedidoForm(request.POST, instance=pedido)
        if form.is_valid():
            form.save()
            return redirect('listar_pedidos')
    else:
        form = PedidoForm(instance=pedido)
    return render(request, 'gestion_pedidos/editar_pedido.html', {'form': form})

# Eliminar un pedido
def eliminar_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    if request.method == 'POST':
        pedido.delete()
        return redirect('listar_pedidos')
    return render(request, 'gestion_pedidos/eliminar_pedido.html', {'pedido': pedido})

# Agregar items a un pedido
def agregar_item_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    if request.method == 'POST':
        form = ItemPedidoForm(request.POST)
        if form.is_valid():
            item_pedido = form.save(commit=False)
            item_pedido.pedido = pedido
            item_pedido.save()
            return redirect('listar_pedidos')
    else:
        form = ItemPedidoForm()
    return render(request, 'gestion_pedidos/agregar_item_pedido.html', {'form': form, 'pedido': pedido})