from django import forms

from .models import Listas, DetalleLista


class UserForm(forms.Form):

    nombre = forms.CharField(label='nombre', max_length=250)


class AddListForm(forms.ModelForm):
    class Meta:
        model = Listas
        fields = ['nombre']


class AddItemForm(forms.ModelForm):
    cantidad = forms.IntegerField(label='cantidad', required=False,
                                  widget=forms.NumberInput(attrs={'placeholder': 'si se requiere'}))
    class Meta:
        model = DetalleLista
        fields = ['nombre', 'cantidad']

