from django import forms
from . models import StartUserWeightAndHeight

class Createinfoform(forms.ModelForm):
    class Meta:
        model = StartUserWeightAndHeight
        fields = ['ime','trenutna_tezina','visina','stepen_gubitka_tezine']