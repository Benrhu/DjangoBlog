from django import forms

class InversionForm(forms.Form):
    amount_invested = forms.DecimalField(label='Cantidad a invertir', max_digits=10, decimal_places=2)
    wallet = forms.CharField(label='Dirección de billetera', max_length=42)