from django.shortcuts import render
from .models import *


def index(request):
    banners = Banner.objects.all()
    return render(request, 'index.html', {"banners": banners})
