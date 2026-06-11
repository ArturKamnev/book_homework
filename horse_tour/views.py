from . import models
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.db.models import F
# Create your views here.

def search_view(request):
    query = request.GET.get('s', '')

    if query:
        tours = models.Tour.objects.filter(title__icontains=query)
    else:
        return HttpResponse('Тур не найден')

    persons = models.Person.objects.all()

    return render(request, 'tours.html',{'tours': tours, 'persons': persons,})

def tour_list_view(request):
    if request.method == "GET":
        tours = models.Tour.objects.all()
        paginator = Paginator(tours, 3)
        page = request.GET.get('page')
        page_obj = paginator.get_page(page)

        persons = models.Person.objects.all()
        context = {
            'tours': page_obj,
            'persons': persons,
        }
    return render(request, template_name='tours.html', context=context)

def tour_list_detailed_view(request, id):
    if request.method == 'GET':
        tour = get_object_or_404(models.Tour, id=id)
        views_tour = request.session.get('viewed_tour', [])

        if id not in views_tour:
            tour.views = F('views') + 1
            views_tour.append(id)
            tour.save()

            tour.refresh_from_db()
        request.session['viewed_tour'] = views_tour

        context = {
                'tour': tour
            }
    return render(request, template_name='tours_detailed.html', context=context)