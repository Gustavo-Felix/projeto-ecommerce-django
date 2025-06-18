from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse
from .models import Produto

class ListaProdutos(ListView):
    model = Produto
    template_name = "produto/listar.html"
    context_object_name = "produtos"
    paginate_by = 10

class DetalheProduto(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Detalhe')

class AdicionarAoCarrinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Adicionar carrinho')

class RemoverDoCarrinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Remover carrinho')

class Carrinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Carrinho')

class Finalizar(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Finalizar')
