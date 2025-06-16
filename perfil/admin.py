from django.contrib import admin
from .models import Perfil

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = 'usuario', 'idade', 'cidade',
    list_display_links = 'usuario',
    search_fields = 'id', 'usuario', 
    list_per_page = 10
    ordering = '-id',