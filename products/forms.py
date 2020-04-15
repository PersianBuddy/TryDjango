from django import forms

from .models import Product

class ProductCreateForm(forms.Form):
    title = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
                            'placeholder': "Your Title",
                         }))
    price = forms.DecimalField(max_digits=6, decimal_places=2)
    summary = forms.CharField(widget=forms.Textarea(attrs={
                            'class': 'my-class',
                            'placeholder': 'Insert some summary about this product',
                        }))

