# forms.py
from django import forms

class SignupForm(forms.Form):
    name = forms.CharField(max_length=150)
    email = forms.EmailField(max_length=50)
    contact = forms.CharField(max_length=10)
    password = forms.CharField(widget=forms.PasswordInput)
