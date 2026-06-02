from django.urls import path
from . import views

urlpatterns = [
    path('products', views.products_list_view, name='products_list'),
    path('categories', views.categories_list_view, name="categories_list"),
    path('products/<int:id>', views.categories_products_list_view, name="categories_product_list")
]