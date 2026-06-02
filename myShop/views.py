from django.shortcuts import render, get_object_or_404
from . import models
# Create your views here.
def products_list_view(request):
    if request.method == "GET":
        products = models.Product.objects.all().order_by("-id")
        context = {
            'products': products
        }
    return render(request, template_name="my_shop/products.html", context=context)

def categories_list_view(request):
    if request.method == "GET":
        categories = models.Category.objects.all().order_by("-id")
        context = {
            "categories": categories
        }
    return render(request, template_name="my_shop/categories.html", context=context)

def categories_products_list_view(request, id):
    if request.method == "GET":
        category_id = get_object_or_404(models.Category, id=id)
        products = models.Product.objects.filter(category=category_id)
        context = {
            "category_id": category_id,
            "products": products,
        }
    return render(request, template_name="my_shop/category_products.html", context=context)