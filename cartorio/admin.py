from django.contrib import admin

from cartorio.models import Estado, Cidade, Bairro, Cartorio


class BairroAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cidade')
    search_fields = ('nome', )
    list_filter = ('cidade',)

class CartAdmin(admin.ModelAdmin):
    list_display = ('nome_oficial', 'nome_fantasia', 'cnpj', 'cidade')
    search_fields = ('cnpj', 'nome_oficial',)
    list_filter = ('cidade__uf', 'cidade', )


# Register your models here.
admin.site.register(Estado)
admin.site.register(Cidade)
admin.site.register(Cartorio, CartAdmin)
admin.site.register(Bairro, BairroAdmin)
