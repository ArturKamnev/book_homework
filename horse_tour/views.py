from . import models
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.db.models import F
# Create your views here.
from django.views import generic

class SearchView(generic.ListView):
    template_name = 'tours.html'
    context_object_name = 'tours'
    model = models.Tour
    paginate_by = 3
    ordering = ['-id']

    def get_queryset(self):
        return self.model.objects.filter(title__icontains=self.request.GET.get('s', ''))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['s'] = self.request.GET.get('s')
        context['persons'] = models.Person.objects.all()
        return context

class TourListView(generic.ListView):
    template_name = 'tours.html'
    model = models.Tour
    paginate_by = 3
    ordering = ['-id']

    def get_queryset(self):
        return self.model.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tours'] = self.model.objects.all()
        context['persons'] = models.Person.objects.all()
        return context

class TourListDetailedView(generic.DetailView):
    pk_url_kwarg = 'id'
    model = models.Tour
    template_name = 'tours_detailed.html'
    context_object_name = 'tour'

    def get_object(self, queryset = None):
        obj = super().get_object(queryset)
        request = self.request
        views_tours = request.session.get('viewed_tour', [])

        if obj.pk not in views_tours:
            self.model.objects.filter(pk=obj.pk).update(views=F('views') + 1)
            views_tours.append(obj.pk)
            request.session['viewed_tour'] = views_tours
            obj.refresh_from_db()
        return obj

