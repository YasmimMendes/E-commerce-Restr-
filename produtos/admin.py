from django.contrib import admin
from produtos.models import Categoria, Produto

# Register your models here.
class ProdutoAdmin(admin.ModelAdmin):
    list_display=('id','nome')

admin.site.register(Categoria)
admin.site.register(Produto, ProdutoAdmin)
