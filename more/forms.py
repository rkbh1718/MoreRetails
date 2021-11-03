from django.core import validators
from django import forms

class UserRegistration(forms.Form):
    
    format = forms.CharField(max_length='20')
    dc_city = forms.CharField()
    location_code =forms.BigIntegerField()
    location_name=forms.CharField(max_length='20')
    activation_date=forms.DateField()