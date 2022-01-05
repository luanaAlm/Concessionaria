from django.shortcuts import render
from .models import *


def index(request):
    bannerPrincipal = Banner1.objects.all()
    bannersSecundarios = Banner2.objects.all()

    return render(request, 'index.html', {"bannerPrincipal": bannerPrincipal, "bannersSecundarios": bannersSecundarios})
