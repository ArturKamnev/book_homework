from django.urls import path
from . import views

urlpatterns = [
    path('create_product/', views.CreateProductView.as_view(), name='create_products'),
    path('products_list/', views.BoughtProductsListView.as_view(), name='products_list'),
    path('delete_products/<int:id>', views.DeleteProductView.as_view(), name='delete_products'),
    path('update_products/<int:id>', views.UpdateProductView.as_view(), name='update_products')
]