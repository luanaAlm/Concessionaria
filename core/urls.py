from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path("carros/<int:ID_Carro>/", views.viewCarros, name="viewCarros"),
    path('cliente_novo/', views.cliente_novo, name='cliente_novo'),
]
