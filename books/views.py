from django.shortcuts import render

# Create your views here.
def book_information(request):
    if request.method == "GET":
        context = {
            'author': 'Джоан Роулинг',
            'universe': 'Гарри Поттер',
            'title': 'Гарри Поттер и Узник Азкабана',
            'date_of_publish': '1999',
        }
    return render(request, 'books_view.html', context)