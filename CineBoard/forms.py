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
        fields = '__all__'

class VipPlaceForm(forms.ModelForm):
    class Meta:
        model = models.VipPlace
        fields = '__all__'

class VipReservationForm(forms.ModelForm):
    class Meta:
        model = models.VipReservation
        fields = '__all__'