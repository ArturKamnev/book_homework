from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list_view, name="book_list"),
    path('<int:id>/', views.book_list_detail_view, name="book_list_detailed")
]