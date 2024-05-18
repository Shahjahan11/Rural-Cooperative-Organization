# forms.py
from django import forms
from .models import Invest

class InvestForm(forms.ModelForm):
    class Meta:
        model = Invest
        fields = ['person', 'description', 'date', 'amount']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
