from django import forms
from . import models

class MovieForm(forms.ModelForm):
    class Meta:
        model = models.Movie
        fields = '__all__'

class GenreForm(forms.ModelForm):
    class Meta:
        model = models.Genre
        fields = '__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ['text']


class VipPlaceForm(forms.ModelForm):
    class Meta:
        model = models.VipSeat
        fields = ['movie', 'seat_number']


class VipReservationForm(forms.ModelForm):
    class Meta:
        model = models.VipReservation
        fields = ['seat']