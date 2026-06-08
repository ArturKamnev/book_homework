from django.shortcuts import render, redirect
from . import models, forms
# Create your views here.
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

def register_view(request):
    if request.method == "POST":
        form = forms.CustomRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/login/')
        
    else:
        form = forms.CustomRegisterForm()
    return render(request=request, template_name='customRegistration/registration.html', context={'form': form})

def auth_login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/candidates_list/')
        
    else:
        form = AuthenticationForm()
    return render(request=request, template_name='customRegistration/login.html', context={'form': form})

def auth_logout_view(request):
    logout(request)
    return redirect('/login/')

def candidates_list_view(request):
    if request.method == "GET":
        candidates = models.CustomUser.objects.all().order_by('-id')
    return render(request=request, template_name='customRegistration/candidates_list.html', context={'candidates': candidates})

