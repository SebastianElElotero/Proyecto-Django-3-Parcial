from django.urls import path
from . import views

urlpatterns = [
    path('recomendaciones/', views.ver_recomendaciones, name='ver_recomendaciones'),
]