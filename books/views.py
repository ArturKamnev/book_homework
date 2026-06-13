from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from . import models
from django.db.models import F
from django.core.paginator import Paginator
from django.views import generic

class SearchView(generic.ListView):
    template_name = 'books_view.html'
    model = models.Books
    context_object_name = 'book'
    paginate_by = 2

    def get_queryset(self):
        return self.model.objects.filter(title__icontains=self.request.GET.get('s', ''))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['s'] = self.request.GET.get('s')
        return context


class BookListView(generic.ListView):
    template_name = 'books_view.html'
    model = models.Books
    ordering = ['-id']
    paginate_by = 2

    def get_queryset(self):
        return self.model.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book'] = models.Books.objects.all()
        context['page_obj'] = context['book']
        return context


class BookDetailView(generic.DetailView):
    template_name = 'books_view_detailed.html'
    model = models.Books
    pk_url_kwarg = 'id'
    context_object_name = 'book_id'

    def get_object(self, queryset = None):
        obj = super().get_object(queryset)
        request = self.request
        views_books = request.session.get('viewed_book', [])

        if obj.pk not in views_books:
            self.model.objects.filter(pk=obj.pk).update(views=F('views') + 1)
            views_books.append(obj.pk)
            request.session['viewed_book'] = views_books
            obj.refresh_from_db()
        return obj
    
