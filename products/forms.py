from django import forms

from .models import Product

class ProductCreateForm(forms.ModelForm):
    title = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
                            'placeholder': "Your Title",
                         }))
    price = forms.DecimalField(max_digits=6, decimal_places=2)
    summary = forms.CharField(widget=forms.Textarea(attrs={
                            'class': 'my-class',
                            'placeholder': 'Insert some summary about this product',
                        }))

    class Meta:
        model = Product
        fields=[
            'title',
            'price',
            'summary'
        ]

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price == 0:
            raise forms.ValidationError("Price must be greater than zero")
        else:
            return price