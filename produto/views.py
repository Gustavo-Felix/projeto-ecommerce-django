from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views import View
from django.http import HttpResponse
from .models import Produto, Variacao

class ListaProdutos(ListView):
    model = Produto
    template_name = "produto/listar.html"
    context_object_name = "produtos"
    paginate_by = 10

class DetalheProduto(DetailView):
    model = Produto
    template_name = "produto/detalhe.html"
    context_object_name = "produto"
    slug_url_kwarg = 'slug' 

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
