from django.shortcuts import render, redirect, get_object_or_404
from . import models, forms
from django.core.paginator import Paginator
# Create your views here.
from django.contrib.auth import login, logout
from django.http import HttpResponse
from django.db.models import F
from django.views import generic


class SearchView(generic.ListView):
    template_name = 'customRegistration/candidates_list.html'
    context_object_name = 'candidates'
    model = models.CustomUser
    paginate_by = 3
    ordering = ['-id']

    def get_queryset(self):
        return self.model.objects.filter(full_name__icontains=self.request.GET.get('s', ''))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['s'] = self.request.GET.get('s')
        return context


class RegisterView(generic.CreateView):
    form_class = forms.CustomRegisterForm
    success_url = '/login/'
    template_name = 'customRegistration/registration.html'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form=form)

class CandidatesListView(generic.ListView):
    model = models.CustomUser
    template_name = 'customRegistration/candidates_list.html'
    paginate_by = 3
    ordering = ['-id']

    def get_queryset(self):
        return self.model.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['candidates'] = models.CustomUser.objects.all()
        return context


class CandidateDetailedView(generic.DetailView):
    model = models.CustomUser
    template_name = 'customRegistration/candidate_detailed.html'
    pk_url_kwarg = 'id'
    context_object_name = 'candidate'

    def get_object(self, queryset = None):
        obj = super().get_object(queryset)
        request = self.request
        views_candidates = request.session.get('viewed_candidate', [])

        if obj.pk not in views_candidates:
            self.model.objects.filter(pk=obj.pk).update(views=F('views') + 1)
            views_candidates.append(obj.pk)
            request.session['viewed_candidate'] = views_candidates
            obj.refresh_from_db()

        return obj
