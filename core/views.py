from django.shortcuts import redirect, render
from .models import *
from core.form import CarroForm, ClienteForm
from django.shortcuts import get_object_or_404


def index(request):
    bannerPrincipal = Banner1.objects.all()
    bannersSecundarios = Banner2.objects.all()
    destaques = Carros.objects.filter(categoria="Destaques")
    seminovos = Carros.objects.all()
    depoimentos = Depoimento.objects.all()
    form = ClienteForm()
    # filtro
    # preco_minimo = request.GET.get('preco_minimo')
    # preco_maximo = request.GET.get('preco_maximo')
    # combustivel = request.GET.get('cidade')
    # cor = request.GET.getlist('tipo')
    # if preco_minimo or preco_maximo or cor or combustivel:

    #     if not preco_minimo:
    #         preco_minimo = 0
    #     if not preco_maximo:
    #         preco_maximo = 999999999
    #     if not combustivel:
    #         combustivel = ['A', 'C']

    #     carros = Carros.objects.filter(valor__gte=preco_minimo)\
    #         .filter(valor__lte=preco_maximo)
    # else:
    #     carros = Carros.objects.all()

    return render(request, 'index.html', {
        "bannerPrincipal": bannerPrincipal,
        "bannersSecundarios": bannersSecundarios,
        "destaques": destaques,
        "seminovos": seminovos,
        "depoimentos": depoimentos,
        "form": form,
    })


def viewCarros(request, ID_Carro):
    data = {}
    carros = Carros.objects.get(ID_Carro=ID_Carro)
    form = CarroForm(request.POST or None, instance=carros)
    form = ClienteForm()
    data["carros"] = carros
    data["form"] = form

    return render(request, "carro.html", data, {"form": form, })


def cliente_novo(request):
    form = ClienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    else:
        return redirect('index')


def cliente_novo_carro(request):
    form = ClienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('carro')
    else:
        # messages.error(
        #     request, 'Houve um erro, reenvie novamente a mensagem!')
        return redirect('carro')
