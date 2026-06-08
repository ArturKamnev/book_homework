from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm
from captcha.fields import CaptchaField

class CustomRegisterForm(UserCreationForm):
    full_name = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=100, initial='+996', required=True)
    date_of_birth = forms.DateField(required=True)
    desired_position = forms.CharField(max_length=100, required=False)
    education = forms.CharField(max_length=50, required=True)
    work_experience = forms.CharField(max_length=300, required=True)
    skills = forms.CharField(max_length=100, required=True)
    captcha = CaptchaField()

    class Meta:
        model = models.CustomUser
        fields = (
            'username',
            'password1',
            'password2',
            'full_name',
            'email',
            'phone_number',
            'date_of_birth',
            'desired_position',
            'education',
            'work_experience',
            'skills',
            'captcha',
        )

    def save(self, commit = True):
        user = super(CustomRegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user