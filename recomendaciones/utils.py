from gestion_productos.models import Producto
from gestion_pedidos.models import Pedido, ItemPedido

def obtener_recomendaciones_para_usuario(usuario):
    # Obtener los productos que el usuario ya compró
    pedidos = Pedido.objects.filter(usuario=usuario).prefetch_related('items')
    productos_comprados = Producto.objects.filter(items__pedido__in=pedidos).distinct()

    # Excluir los productos ya comprados de las recomendaciones
    productos_recomendados = Producto.objects.exclude(id__in=productos_comprados).order_by('?')[:5]  # Recomienda 5 productos al azar

    return productos_recomendados