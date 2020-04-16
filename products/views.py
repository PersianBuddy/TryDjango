from django.http import Http404
from django.shortcuts import render , get_object_or_404 , redirect
from products.models import Product
from products.forms import ProductCreateForm
# Create your views here.

def products_list_view(request, *args, **kwargs):
    querrylist = Product.objects.all()
    context = {
        'products_list' : querrylist,
    }
    return render(request, 'products/products_list.html',context)

def product_detail_view(request,my_id, *args, **kwargs):
    try:
        product_object = Product.objects.get(id = my_id)
    except Product.DoesNotExist:
        raise Http404
    context ={
        "product_object" : product_object,
    }
    return render(request,'products/product_detail.html',context)

def create_product_view(request, *args, **kwargs):
    product_create_form = ProductCreateForm()
    if request.method == 'POST':
        product_create_form = ProductCreateForm(request.POST)
        if product_create_form.is_valid():
           product_create_form.save()
           product_create_form = ProductCreateForm()
        else:
            print(product_create_form.errors)#print errors in console
    context = {
        'form' : product_create_form,
    }
    return render(request,'products/create_product.html',context)

def delete_product_view(request, product_id, *args, **kwargs):
    product_object = get_object_or_404(Product, id =product_id)
    if request.method == 'POST':
        product_object.delete()
        return redirect('../../')
    context ={
        'product_object':product_object,
    }
    return render(request, 'products/delete_product.html',context)