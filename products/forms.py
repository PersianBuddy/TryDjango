from django import forms

from .models import Product

class ProductCreateForm(forms.Form):
    title = forms.CharField(max_length=100)
    price = forms.DecimalField(max_digits=6, decimal_places=2)
    summary = forms.CharField()

