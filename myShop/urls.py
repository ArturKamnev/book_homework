from django.urls import path
from . import views

urlpatterns = [
    path('products', views.ProductListView.as_view(), name='products_list'),
    path('categories', views.CategoryListView.as_view(), name="categories_list"),
    path('products/<int:id>', views.ProductsOfCategoryListView.as_view(), name="categories_product_list")
]