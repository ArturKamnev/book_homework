from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from . import models

# Create your views here.
def book_list_view(request):
    if request.method == "GET":
        book = models.Books.objects.all().order_by('-id')
        context = {
            'book': book,
        }
    return render(request=request, template_name='books_view.html', context=context)

def book_list_detail_view(request, id):
    if request.method == "GET":
        book_id = get_object_or_404(models.Books, id=id)
        context = {
            'book_id': book_id,
        }
    return render(request=request, template_name='books_view_detailed.html', context=context)