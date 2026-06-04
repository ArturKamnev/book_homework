from django.shortcuts import render, redirect, get_object_or_404
from . import models, forms
# Create your views here.

def bought_products_list_view(request):
    if request.method == "GET":
        products = models.Product.objects.all().order_by('-id')
        context = {
            'products': products
        }
    return render(request, template_name='basket/products_list.html', context=context)

def create_products(request):
    if request.method == "POST":
        form = forms.ProductsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('products_list')
    else:
        form = forms.ProductsForm()

    context = {
        'form': form
    }
    return render(request, template_name='basket/create_product.html', context=context)

def delete_products(request, id):
    game_id = get_object_or_404(models.Product, id=id)
    game_id.delete()
    return redirect('products_list')

def update_products(request, id):
    product_id = get_object_or_404(models.Product, id=id)
    if request.method == "POST":
        form = forms.ProductsForm(request.POST, request.FILES, instance=product_id)
        if form.is_valid():
            form.save()
            return redirect('products_list')
    else:
        form = forms.ProductsForm(instance=product_id)
    context = {
        'form': form,
        'product_id': product_id
    }
    return render(request, template_name='basket/update_product.html', context=context)