from django.shortcuts import render, redirect, get_object_or_404
from . import models, forms
from django.views import generic
# Create your views here.

class BoughtProductsListView(generic.ListView):
    template_name = 'basket/products_list.html'
    model = models.Product
    context_object_name = 'products'

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CreateProductView(generic.CreateView):
    success_url = '/products_list/'
    form_class = forms.ProductsForm
    template_name = 'basket/create_product.html'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateProductView, self).form_valid(form=form)
    



class DeleteProductView(generic.DeleteView):
    success_url = '/products_list/'
    model = models.Product
    template_name = 'basket/confirm_delete.html'
    context_object_name = 'product_id'

    def get_object(self, **kwargs):
        product_id = self.kwargs.get('id')
        return get_object_or_404(self.model, id=product_id)



class UpdateProductView(generic.UpdateView):
    template_name = 'basket/update_product.html'
    form_class = forms.ProductsForm
    model = models.Product
    success_url = '/products_list/'

    def get_object(self, **kwargs):
        product_id = self.kwargs.get('id')
        return get_object_or_404(self.model, id=product_id)
    
    def form_valid(self, form):
        print(form.cleaned_data)
        return super(UpdateProductView, self).form_valid(form=form)
        

