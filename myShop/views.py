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
        return context


class CategoryListView(generic.ListView):
    template_name = 'my_shop/categories.html'
    model = models.Category
    ordering = ['-id']

    def get_queryset(self):
        return self.model.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

# Create your views here.

class ProductsOfCategoryListView(generic.ListView):
    template_name = 'my_shop/category_products.html'
    model = models.Product
    context_object_name = 'products'

    def get_queryset(self):
        id_val = self.kwargs.get('id')
        category = get_object_or_404(models.Category, id=id_val)
        return self.model.objects.filter(category=category).order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id_val = self.kwargs.get('id')
        context['category'] = get_object_or_404(models.Category, id=id_val)
        return context
