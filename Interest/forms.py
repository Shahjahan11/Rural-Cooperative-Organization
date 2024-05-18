# forms.py
from django import forms
from .models import Interest

class InterestForm(forms.ModelForm):
    class Meta:
        model = Interest
        fields = ['person', 'description', 'date', 'amount']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
