from django.shortcuts import render
from .models import *
from core.form import CarroForm


def index(request):
    bannerPrincipal = Banner1.objects.all()
    bannersSecundarios = Banner2.objects.all()
    destaques = Carros.objects.filter(categoria="Destaques")
    seminovos = Carros.objects.filter(categoria="Seminovos")
    return render(request, 'index.html', {
        "bannerPrincipal": bannerPrincipal,
        "bannersSecundarios": bannersSecundarios,
        "destaques": destaques,
        "seminovos": seminovos,
    })


def viewCarros(request, ID_Carro):
    data = {}
    carros = Carros.objects.get(ID_Carro=ID_Carro)
    form = CarroForm(request.POST or None, instance=carros)
    data["carros"] = carros
    data["form"] = form
    return render(request, "carro.html", data)
