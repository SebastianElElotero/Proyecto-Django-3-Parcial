from django.db import models
from gestion_usuarios.models import Usuario

class Administrador(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    rol = models.CharField(max_length=50, default='Administrador')

    def __str__(self):
        return f"Administrador: {self.usuario.username}"