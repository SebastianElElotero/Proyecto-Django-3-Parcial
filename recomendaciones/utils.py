from gestion_productos.models import Producto
from gestion_pedidos.models import Pedido, ItemPedido
from .models import Recomendacion

def obtener_recomendaciones_para_usuario(request):
    # Obtener los productos que el usuario ya compró
    #print(request.__dict__)
    pedido = Recomendacion.objects.filter(usuario=request).last()
    #itemspedido = ItemPedido.objects.filter(pedido=pedido)
    #print(itemspedido)
    print(pedido.__dict__)
    productos_comprados = Producto.objects.filter(id=pedido.producto_id).distinct()

    # Excluir los productos ya comprados de las recomendaciones
    productos_recomendados = Producto.objects.exclude(id__in=productos_comprados).order_by('?')[:5]  # Recomienda 5 productos al azar
    print(productos_recomendados)
    return productos_recomendados