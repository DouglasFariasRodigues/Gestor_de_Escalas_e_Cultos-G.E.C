from django.contrib import admin
from .models import Obreiro, Local, NatCulto, Culto, Escala, EscalaItem

@admin.register(Obreiro)
class ObreiroAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'ativo')
    list_filter = ('ativo', 'cargo')
    search_fields = ('nome',)

@admin.register(Local)
class LocalAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ativo')
    list_filter = ('ativo',)
    search_fields = ('nome',)

@admin.register(NatCulto)
class NatCultoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ativo')
    list_filter = ('ativo',)
    search_fields = ('nome',)

@admin.register(Culto)
class CultoAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'data_hora', 'local', 'nat_culto')
    list_filter = ('local', 'nat_culto', 'data_hora')
    date_hierarchy = 'data_hora'
    search_fields = ('local__nome', 'nat_culto__nome')

# Configuração para editar Itens da Escala dentro da própria Escala
class EscalaItemInline(admin.TabularInline):
    model = EscalaItem
    extra = 1  # Mostra 1 linha vazia extra para adição rápida
    autocomplete_fields = ['obreiro', 'culto'] # Útil se tivermos muitos registros

@admin.register(Escala)
class EscalaAdmin(admin.ModelAdmin):
    list_display = ('mes', 'ano', 'status')
    list_filter = ('ano', 'status')
    inlines = [EscalaItemInline]

@admin.register(EscalaItem)
class EscalaItemAdmin(admin.ModelAdmin):
    list_display = ('escala', 'culto', 'obreiro')
    list_filter = ('escala__mes', 'escala__ano')
    search_fields = ('obreiro__nome',)
