from django import forms
from .models import Pedido, ItemPedido

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['estado']

class ItemPedidoForm(forms.ModelForm):
    class Meta:
        model = ItemPedido
        fields = ['producto', 'cantidad']
