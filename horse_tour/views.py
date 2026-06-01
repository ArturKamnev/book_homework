from . import models
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# Create your views here.

def tour_list_view(request):
    if request.method == "GET":
        tours = models.Tour.objects.all()
        persons = models.Person.objects.all()
        context = {
            'tours': tours,
            'persons': persons,
        }
    return render(request, template_name='tours.html', context=context)