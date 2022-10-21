from django import forms
from . models import StartUserWeightAndHeight, CurrentWeight

class CreateInfoForm(forms.ModelForm):
    class Meta:
        model = StartUserWeightAndHeight
        fields = ['ime','pocetna_tezina','visina','stepen_gubitka_tezine', 'pol']
        widgets = {
               'pol': forms.RadioSelect()
           }   



class AddCurrentWeight(forms.ModelForm):
    class Meta:
        model = CurrentWeight
        fields = ['trenutna_tezina','detalji']