from django.shortcuts import render
from products.models import Product
# Create your views here.
def product_detail_view(request, *args, **kwargs):
    product_object = Product.objects.get(id = 2)
    context ={
        "product_object" : product_object,
    }
    return render(request,'products/product_detail.html',context)

def create_product_view(request, *args, **kwargs):
    context = {}
    return render(request,'products/create_product.html',context)