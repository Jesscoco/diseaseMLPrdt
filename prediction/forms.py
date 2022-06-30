from .models import Historics
from django import forms
class HistoricsForm(forms.ModelForm):
   class Meta:
      model = Historics
      fields = ['name','symptom_n1','symptom_n2','symptom_n3']
      widgets = {
         'name':forms.TextInput(attrs= {'class':'form-control'}),
         'symptom_n1':forms.Select(attrs= {'class':'form-control'}),
         'symptom_n2':forms.Select(attrs= {'class':'form-control'}),
         'symptom_n3':forms.Select(attrs= {'class':'form-control'}),



      }
   