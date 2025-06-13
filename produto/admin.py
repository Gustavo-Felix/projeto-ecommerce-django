from django.contrib import admin
from .models import Produto, Variacao

class VariacaoInline(admin.TabularInline):
    model = Variacao
    extra = 1

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = 'nome', 'descricao_curta', 'preco_marketing',
    list_display_links = 'nome',
    search_fields = 'id', 'nome', 
    list_per_page = 10
    ordering = '-id',
    inlines = [VariacaoInline]

admin.site.register(Variacao)