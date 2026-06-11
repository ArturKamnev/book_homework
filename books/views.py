from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from . import models
from django.db.models import F
from django.core.paginator import Paginator

def search_view(request):
    query = request.GET.get('s', '')
    if query:
        book = models.Books.objects.filter(title__icontains=query)
    else:
        return HttpResponse("Книга не найдена")
    return render(request, template_name='books_view.html', context={'book': book})

# Create your views here.
def book_list_view(request):
    if request.method == "GET":
        book = models.Books.objects.all().order_by('-id')
        paginator = Paginator(book, 2)
        page = request.GET.get('page')
        page_obj = paginator.get_page(page)
        context = {
            'book': page_obj,
        }
    return render(request=request, template_name='books_view.html', context=context)

def book_list_detail_view(request, id):
    if request.method == "GET":
        book_id = get_object_or_404(models.Books, id=id)
        views_book = request.session.get('viewed_book', [])

        if id not in views_book:
            book_id.views = F('views') + 1
            views_book.append(id)
            book_id.save()
            book_id.refresh_from_db()
        request.session['viewed_book'] = views_book


        context = {
            'book_id': book_id,
        }
    return render(request=request, template_name='books_view_detailed.html', context=context)