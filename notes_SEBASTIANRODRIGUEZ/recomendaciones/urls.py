from django.urls import path
from . import views
app_name = "recomendaciones"

urlpatterns = [
    path('recomendaciones/', views.ver_recomendaciones, name='ver_recomendaciones'),
]