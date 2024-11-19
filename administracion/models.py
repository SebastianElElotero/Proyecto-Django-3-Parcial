from django.db import models
from django.contrib.auth.models import User

class Administrador(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    rol = models.CharField(max_length=50, default='Administrador')

    def __str__(self):
        return f"Administrador: {self.usuario.username}"