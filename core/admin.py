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


admin.site.register(Cliente)
admin.site.register(Banner1)
admin.site.register(Banner2)
admin.site.register(Depoimento)
