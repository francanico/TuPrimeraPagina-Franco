from django import forms
from .models import Poliza, Usuario,Auto

class PolizaForm(forms.ModelForm):
    class Meta:
        model = Poliza
        fields =["nombre","precio","categoria"]

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields =["nombre","edad","registro"]
    
class AutoForm(forms.ModelForm):
    class Meta:
        model= Auto
        fields = ["marca","modelo","color","placa","kilometraje"]