from django.shortcuts import render, get_object_or_404, redirect
from .models import Pago
from .forms import PagoForm

# Listar pagos
def listar_pagos(request):
    pagos = Pago.objects.filter(usuario=request.user)
    return render(request, 'gestion_pagos/listar_pagos.html', {'pagos': pagos})

# Crear un nuevo pago
def crear_pago(request):
    if request.method == 'POST':
        form = PagoForm(request.POST)
        if form.is_valid():
            pago = form.save(commit=False)
            pago.usuario = request.user
            pago.save()
            return redirect('listar_pagos')
    else:
        form = PagoForm()
    return render(request, 'gestion_pagos/crear_pago.html', {'form': form})

# Editar un pago existente
def editar_pago(request, pago_id):
    pago = get_object_or_404(Pago, id=pago_id)
    if request.method == 'POST':
        form = PagoForm(request.POST, instance=pago)
        if form.is_valid():
            form.save()
            return redirect('listar_pagos')
    else:
        form = PagoForm(instance=pago)
    return render(request, 'gestion_pagos/editar_pago.html', {'form': form})