from django.contrib import admin
from .models import Pedido, ItemPedido

class ItemPedidoInline(admin.TabularInline):
    model = ItemPedido
    extra = 1

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = 'usuario', 'total', 'status',
    list_display_links = 'usuario',
    search_fields = 'id', 'usuario', 
    list_per_page = 10
    ordering = '-id',
    inlines = ItemPedidoInline,

admin.site.register(ItemPedido)