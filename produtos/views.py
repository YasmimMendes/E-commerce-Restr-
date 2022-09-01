from django.shortcuts import render
from produtos.models import Produto

# Create your views here.

def index(request):
    lista = Produto.objects.all()
    context = {'produtos' : lista}
    return render(request,'index.html', context)

# def lista_produtos(request):
#     lista = Produto.objects.all()
#     return render(request,'produtos.html')
