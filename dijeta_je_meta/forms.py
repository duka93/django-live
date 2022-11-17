from django import forms
from . models import StartUserWeightAndHeight, CurrentWeight

class CreateInfoForm(forms.ModelForm):
    class Meta:
        model = StartUserWeightAndHeight
        fields = ['ime','visina','pocetna_tezina', 'pol']
        widgets = {
               'pol': forms.RadioSelect()
           }
  

class AddCurrentWeight(forms.ModelForm):
    class Meta:
        model = CurrentWeight
        fields = ['trenutna_tezina','detalji']



class UpdateStartWeightAndHeight(forms.ModelForm):
    class Meta:
      model = StartUserWeightAndHeight
      fields = ['ime', 'pocetna_tezina', 'visina']


  



class UpdateWeightForm(forms.ModelForm):
    class Meta:
        model = CurrentWeight
        fields = ['trenutna_tezina', 'detalji']
