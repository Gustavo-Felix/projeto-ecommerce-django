from django.contrib import admin
from .models import Produto, Variacao

class VariacaoInline(admin.TabularInline):
    model = Variacao
    extra = 1

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = 'nome', 'descricao_curta_resumida', 'get_preco_formatado', 'get_preco_promocional_formatado'
    list_display_links = 'nome',
    search_fields = 'id', 'nome', 
    list_per_page = 10
    ordering = '-id',
    inlines = [VariacaoInline]

    def descricao_curta_resumida(self, model):
        return (model.descricao_curta[:75] + '...') if len(model.descricao_curta) > 75 else model.descricao_curta
    descricao_curta_resumida.short_description = 'Descrição Curta'
    
admin.site.register(Variacao)