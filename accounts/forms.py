from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

        labels = {
            'username': '',
            'first_name': '',
            'last_name': '',
            'email': '',
            'password1': '',
            'password2': '',
        }
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'}),
            'first_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}),
            'last_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}),
            'email': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email'}),
            'password1': forms.PasswordInput(attrs={'class':'form-control form-input', 'placeholder':'Password', 'type': 'password'}),
            'password2': forms.PasswordInput(attrs={'class':'form-control form-input', 'placeholder':'Confirm Password', 'type': 'password'}),
        }
