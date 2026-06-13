from django.shortcuts import render, get_object_or_404
from . import models
from django.views import generic

class ProductListView(generic.ListView):
    template_name = 'my_shop/products.html'
    ordering = ['-id']
    model = models.Product

    def get_queryset(self):
        return self.model.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = self.model.objects.all()
        return context


class CategoryListView(generic.ListView):
    template_name = 'my_shop/categories.html'
    model = models.Category
    ordering = ['-id']

    def get_queryset(self):
        return self.model.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = self.model.objects.all()

# Create your views here.

class ProductsOfCategoryListView(generic.ListView):
    ordering = ['-id']
    template_name = 'my_shop/category_products.html'
    model = models.Product

    def get_queryset(self):
        id_val = self.kwargs.get('id')
        category = get_object_or_404(models.Category, id=id_val)
        return self.model.objects.filter(category=category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id_val = self.kwargs.get('id')
        category = get_object_or_404(models.Category, id=id_val)
        products = self.model.objects.filter(category=category)
        context['category'] = category
        context['products'] = products
        return context


def categories_products_list_view(request, id):
    if request.method == "GET":
        category_id = get_object_or_404(models.Category, id=id)
        products = models.Product.objects.filter(category=category_id)
        context = {
            "category_id": category_id,
            "products": products,
        }
    return render(request, template_name="my_shop/category_products.html", context=context)