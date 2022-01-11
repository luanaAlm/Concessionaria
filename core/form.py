from django.forms import ModelForm
from .models import Carros
from .models import Cliente


class CarroForm(ModelForm):
    class Meta:
        model = Carros
        fields = "__all__"


class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
