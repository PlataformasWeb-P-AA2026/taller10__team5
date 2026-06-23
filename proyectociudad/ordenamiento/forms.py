
from django.forms import ModelForm
from django import forms

from ordenamiento.models import Parroquia,Barrio, \
        PresidenteBarrio
class ParroquiaForm(ModelForm):
    class Meta:
        model = Parroquia
        fields = ['nombre', 'ubicacion', 'tipo'] 

class BarrioForm(ModelForm):
    class Meta:
        model = Barrio
        fields = ['nombre', 'numero_viviendas', 'numero_parques','numero_edificios_residenciales','parroquia'] 

# class PresidenteBarrioForm(ModelForm):
#     class Meta:
#         model = PresidenteBarrio
#         fields = ['cedula', 'nickname', 'edad','profesion','barrio'] 

