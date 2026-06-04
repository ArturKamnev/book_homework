from django.urls import path
from . import views

urlpatterns = [
    path('create_product/', views.create_products, name='create_products'),
    path('products_list/', views.bought_products_list_view, name='products_list'),
    path('delete_products/<int:id>', views.delete_products, name='delete_products'),
    path('update_products/<int:id>', views.update_products, name='update_products')
]