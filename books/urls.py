from django.urls import path
from . import views

urlpatterns = [
    path('books', views.book_list_view, name="book_list"),
    path('books/<int:id>', views.book_list_detail_view, name="book_list_detailed")
]