from django.db import models
from gestion_usuarios.models import Usuario
from gestion_pedidos.models import Pedido

class Pago(models.Model):
    METODOS_PAGO = [
        ('T', 'Tarjeta de Crédito'),
        ('P', 'PayPal'),
        ('D', 'Depósito Bancario'),
    ]

    ESTADO_PAGO = [
        ('P', 'Pendiente'),
        ('C', 'Completado'),
        ('F', 'Fallido'),
    ]

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    metodo_pago = models.CharField(max_length=1, choices=METODOS_PAGO)
    estado = models.CharField(max_length=1, choices=ESTADO_PAGO, default='P')
    fecha_pago = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pago {self.id} de {self.usuario.username} - {self.get_metodo_pago_display()}"