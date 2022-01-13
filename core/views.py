from django.shortcuts import redirect, render
from .models import *
from core.form import CarroForm, ClienteForm


def index(request):
    bannerPrincipal = Banner1.objects.all()
    bannersSecundarios = Banner2.objects.all()
    destaques = Carros.objects.filter(categoria="Destaques")
    seminovos = Carros.objects.filter(categoria="Seminovos")
    depoimentos = Depoimento.objects.all()

    form = ClienteForm()

    return render(request, 'index.html', {
        "bannerPrincipal": bannerPrincipal,
        "bannersSecundarios": bannersSecundarios,
        "destaques": destaques,
        "seminovos": seminovos,
        "depoimentos": depoimentos,
        "form": form
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
        # messages.success(request, 'Sua mensagem foi enviada com sucesso!')
        return redirect('index')
    else:
        # messages.error(
        #     request, 'Houve um erro, reenvie novamente a mensagem!')
        return redirect('index')


def cliente_novo_carro(request):
    form = ClienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        # messages.success(request, 'Sua mensagem foi enviada com sucesso!')
        return redirect('carro')
    else:
        # messages.error(
        #     request, 'Houve um erro, reenvie novamente a mensagem!')
        return redirect('carro')
