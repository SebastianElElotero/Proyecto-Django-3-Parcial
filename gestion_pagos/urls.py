from django.urls import path
from . import views
app_name = "gestion_pagos"

urlpatterns = [
    path('pagos/', views.listar_pagos, name='listar_pagos'),
    path('pagos/crear/', views.crear_pago, name='crear_pago'),
    path('pagos/editar/<int:pago_id>/', views.editar_pago, name='editar_pago'),
]