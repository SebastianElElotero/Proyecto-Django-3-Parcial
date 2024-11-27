from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto, Categoria
from .forms import ProductoForm, CategoriaForm

# Listar productos
def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'gestion_productos/listar_productos.html', {'productos': productos})

# Agregar un producto
def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gestion_productos:listar_productos')
    else:
        form = ProductoForm()
    return render(request, 'gestion_productos/agregar_producto.html', {'form': form})

# Editar un producto
def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('gestion_productos:listar_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'gestion_productos/editar_producto.html', {'form': form})

# Eliminar un producto
def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        producto.delete()
        return redirect('gestion_productos:listar_productos')
    return render(request, 'gestion_productos/eliminar_producto.html', {'producto': producto})

# Listar categorías
def listar_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'gestion_productos/listar_categorias.html', {'categorias': categorias})

# Agregar una categoría
def agregar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gestion_productos:listar_categorias')
    else:
        form = CategoriaForm()
    return render(request, 'gestion_productos/agregar_categoria.html', {'form': form})