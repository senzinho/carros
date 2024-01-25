from django.contrib import admin
from cars.models import Car, Brand #importando cars.models

#registrando em nosso admin de carros

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class CarAdmin(admin.ModelAdmin):
    list_display = ('model','brand','factory_year','model_year','value') #para grade (tipo um menu)
    search_fields = ('model','brand') #campo de busca






admin.site.register(Brand, BrandAdmin)
admin.site.register(Car,CarAdmin)#pede dois parametros 1°Qual tabela do DB e qual o Admin para registro(config)


    