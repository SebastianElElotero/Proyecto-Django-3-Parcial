from django.shortcuts import render
from .utils import obtener_recomendaciones_para_usuario

def ver_recomendaciones(request):
    print(request.user)
    recomendaciones = obtener_recomendaciones_para_usuario(request.user)
    productos = []
    for producto in recomendaciones:
        productos.append(producto[0])
    print("Recomendaciones")
    print(productos)  # Verifica qué devuelve esta función
    return render(request, 'recomendaciones/ver_recomendaciones.html', {'recomendaciones': productos})
