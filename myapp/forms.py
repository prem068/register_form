from django import forms
from myapp.models import *

class EmployeeForms(forms.ModelForm):
    phno = forms.IntegerField(
        min_value=1000000000,  
        max_value=9999999999,  
        widget=forms.NumberInput(attrs={
            'class': 'rounded-xl border-gray-300 focus:ring-blue-500 focus:border-blue-500 w-full px-4 py-2',
            'placeholder': 'Enter your phone number',
            'type': 'number'  
        })
       
    )
    class Meta:
        model=Employee
        fields='__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'rounded-xl border-gray-300 focus:ring-blue-500 focus:border-blue-500 w-full px-4 py-2',
                'placeholder': 'Enter your name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'rounded-xl border-gray-300 focus:ring-blue-500 focus:border-blue-500 w-full px-4 py-2',
                'placeholder': 'Enter your email'

            }),
            'dob': forms.DateInput(attrs={
                'class': 'rounded-xl border-gray-300 focus:ring-blue-500 focus:border-blue-500 w-full px-4 py-2',
                'placeholder': 'YYYY-MM-DD',
                'type': 'date'
            }),
        
            'addr': forms.TextInput(attrs={
                'class': 'rounded-xl border-gray-300 focus:ring-blue-500 focus:border-blue-500 w-full px-4 py-2',
                'placeholder': 'Enter your address'
            }),
        }