from django import forms
from TiendaApp.models import producto,trabajadores,clientes

class ProductoForm(forms.ModelForm):
    class Meta:
        model = producto
        fields = '__all__'

class ClienteForm(forms.ModelForm):
    class Meta:
        model = clientes
        fields = '__all__'

class TrbajadorForm(forms.ModelForm):
    class Meta:
        model = trabajadores
        fields = '__all__'
