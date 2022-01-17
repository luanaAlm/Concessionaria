from django.contrib import admin
from .models import *


@admin.register(Carros)
class CarroAdmin(admin.ModelAdmin):
    list_display = ('marca', 'Modelo', 'AnoInicial',
                    'AnoFinal', 'porta', 'combustivel', 'finalPlaca', 'cor', 'valor')
    search_fields = ('marca', 'Modelo', 'AnoInicial',
                     'AnoFinal', 'porta', 'combustivel', 'finalPlaca', 'cor', 'valor')
    list_filter = ('marca', 'Modelo', 'AnoInicial',
                   'AnoFinal', 'porta', 'combustivel', 'finalPlaca', 'cor', 'valor',)


@admin.register(Depoimento)
class DepoimentoAdmin(admin.ModelAdmin):
    list_display = ('ID_Depoimentos', 'nome')
    search_fields = ('ID_Depoimentos', 'nome',)
    list_filter = ('nome',)


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone', 'mensagem')
    search_fields = ('nome', 'email', 'telefone', 'mensagem',)
    list_filter = ('nome', 'email', 'telefone', 'mensagem',)


admin.site.register(Banner1)
admin.site.register(Banner2)
