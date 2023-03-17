from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Investor

class InvestorCreationForm(UserCreationForm):
    name = forms.CharField(max_length=30, required=True, help_text='Required.')
    surname = forms.CharField(max_length=30, required=True, help_text='Required.')
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Enter a valid email address.')

    class Meta:
        model = Investor
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')