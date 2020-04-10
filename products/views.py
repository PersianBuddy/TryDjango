from django.shortcuts import render
from products.models import Product
# Create your views here.
def product_detail_view(request, *args, **kwargs):
    product_object = Product.objects.get(id = 2)
    context ={
        "product_object" : product_object,
    }
    return render(request,'product/detail.html',context)