from django.urls import path
from . import views

urlpatterns = [
    path('books', views.BookListView.as_view(), name="book_list"),
    path('books/<int:id>', views.BookDetailView.as_view(), name="book_list_detailed"),
    path('books/search/', views.SearchView.as_view(), name='books_search')
]