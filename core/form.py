from django.forms import ModelForm
from .models import Carros


class CarroForm(ModelForm):
    class Meta:
        model = Carros
        fields = "__all__"
