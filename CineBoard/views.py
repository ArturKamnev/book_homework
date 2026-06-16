from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from . import models
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from . import forms
# from django.contrib.auth.models import User
# Create your views here.

class MovieListView(generic.ListView):
    template_name = 'cineboard/movies_view.html'
    context_object_name = 'movies'
    model = models.Movie

    def get_queryset(self):
        return self.model.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        genre = models.Genre.objects.all()
        context['genres'] = genre
        return context
    
class MovieDetailedView(generic.DetailView):
    template_name = 'cineboard/movies_detailed.html'
    pk_url_kwarg = 'id'
    context_object_name = 'movie'
    model = models.Movie

    def get_object(self, queryset = None):
        obj = super().get_object(queryset)
        return obj
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comment = models.Comment.objects.filter(movie=self.object)
        vip_place = models.VipPlace.objects.filter(movie=self.object)
        reservation = models.VipReservation.objects.filter(seat=vip_place)
        context['vip_places'] = vip_place
        context['reservations'] = reservation
        context['comments'] = comment
        return context
    
class MovieSearchView(generic.ListView):
    template_name = 'cineboard/movies_view.html'
    context_object_name = 'movies'
    model = models.Movie

    def get_queryset(self):
        return self.model.objects.filter(title__icontains=self.request.GET.get('s', ''))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['s'] = self.request.GET.get('s')
        return context
    
class UserRegisterView(generic.CreateView):
    template_name = 'cineboard/register.html'
    success_url = '/movie/user_auth/'
    form_class = UserCreationForm

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form=form)
    

class MovieCreateView(generic.CreateView):
    template_name = 'cineboard/create_movie.html'
    success_url = '/movies_list/'
    form_class = forms.MovieForm

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form=form)
    
class MovieUpdateView(generic.UpdateView):
    form_class = forms.MovieForm
    template_name = 'cineboard/update_movie.html'
    success_url = '/movies_list/'
    model = models.Movie
    

    def get_object(self, **kwargs):
        movie_id = self.kwargs.get('id')
        return get_object_or_404(self.model, id=movie_id)
    
    def form_valid(self, form):
        print(form.cleaned_data)
        return super(MovieUpdateView, self).form_valid(form=form)

class MovieDeleteView(generic.DeleteView):
    success_url = '/movies_list/'
    model = models.Movie
    template_name = 'cineboard/confirm_delete.html'
    context_object_name = 'movie_id'

    def get_object(self, **kwargs):
        movie_id = self.kwargs.get('id')
        return get_object_or_404(self.model, id=movie_id)
    
class GenreCreateView(generic.CreateView):
    success_url = '/movies_list/'
    template_name = 'cineboard/create_genre.html'
    form_class = forms.GenreForm

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form=form)
    
class MoviesOfGenreView(generic.ListView):
    template_name = 'cineboard/movies_view.html'
    context_object_name = 'movies'
    model = models.Movie

    def get_queryset(self, **kwargs):
        genre_id = self.kwargs.get('id')
        return self.model.objects.filter(genre=genre_id)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        genre = models.Genre.objects.all()
        context['genres'] = genre
        return context
    
class CreateCommentView(generic.CreateView):
    success_url = '/movies_list/'
    template_name = 'cineboard/create_comment.html'
    form_class = forms.CommentForm

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form=form)
    
class CreateVipPlace(generic.CreateView):
    template_name = 'cineboard/create_vip_place.html'
    success_url = '/movies_list/'
    form_class = forms.VipPlaceForm

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form=form)
    
class ReservVipPlace(generic.CreateView):
    template_name = 'cineboard/reserv_vip_place.html'
    success_url = '/movies_list/'
    form_class = forms.VipReservationForm

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)