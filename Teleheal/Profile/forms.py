from django import forms
from .models import PatientProfile

class PatientProfileForm(forms.ModelForm):
    class Meta:
        model = PatientProfile
        fields = ['age', 'email', 'country_of_origin', 'gender']
        widgets = {
            'age': forms.TextInput(attrs={'readonly': 'readonly'}),
            'email': forms.TextInput(attrs={'readonly': 'readonly'}),
            'country_of_origin': forms.TextInput(attrs={'readonly': 'readonly'}),
            'gender': forms.TextInput(attrs={'readonly': 'readonly'}),
        }
