from django.db import models
from gestion_productos.models import Producto
from gestion_usuarios.models import Usuario

class Recomendacion(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    fecha_recomendacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Recomendación de {self.producto.nombre} para {self.usuario.username}"