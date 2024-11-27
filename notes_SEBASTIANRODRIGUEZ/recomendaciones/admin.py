from django.contrib import admin
from .models import Recomendacion

@admin.register(Recomendacion)
class RecomendacionAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'producto')  # Elimina 'recomendado_en' si no existe
