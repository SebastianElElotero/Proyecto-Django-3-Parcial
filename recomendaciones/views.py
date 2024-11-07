from django.shortcuts import render
from .utils import obtener_recomendaciones_para_usuario

def ver_recomendaciones(request):
    recomendaciones = obtener_recomendaciones_para_usuario(request.user)
    return render(request, 'recomendaciones/ver_recomendaciones.html', {'recomendaciones': recomendaciones})