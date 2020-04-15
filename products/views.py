from django.shortcuts import render
from products.models import Product
from products.forms import ProductCreateForm
# Create your views here.
def product_detail_view(request, *args, **kwargs):
    product_object = Product.objects.get(id = 2)
    context ={
        "product_object" : product_object,
    }
    return render(request,'products/product_detail.html',context)

def create_product_view(request, *args, **kwargs):
    product_create_form = ProductCreateForm()
    if request.method == 'POST':
        product_create_form = ProductCreateForm(request.POST)
        if product_create_form.is_valid():
            Product.objects.create(**product_create_form.cleaned_data)
        else:
            print(product_create_form.errors)#print errors in console
    context = {
        'form' : product_create_form,
    }
    return render(request,'products/create_product.html',context)