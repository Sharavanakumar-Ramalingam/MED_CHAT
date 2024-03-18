from django import forms

class SymptomForm(forms.Form):
    symptoms = forms.CharField(label='Symptoms', max_length=100)
