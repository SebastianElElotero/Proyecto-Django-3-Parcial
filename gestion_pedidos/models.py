from django.db import models
from gestion_productos.models import Producto
from gestion_usuarios.models import Usuario  # Asegúrate de que tienes un modelo de usuario

class Pedido(models.Model):
    ESTADOS_PEDIDO = [
        ('P', 'Pendiente'),
        ('E', 'Enviado'),
        ('C', 'Completado'),
        ('A', 'Anulado'),
    ]

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=1, choices=ESTADOS_PEDIDO, default='P')

    def __str__(self):
        return f"Pedido {self.id} de {self.usuario.username}"

class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='items')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()

    def subtotal(self):
        return self.cantidad * self.producto.precio

