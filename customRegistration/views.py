from django.shortcuts import render, redirect, get_object_or_404
from . import models, forms
from django.core.paginator import Paginator
# Create your views here.
from django.contrib.auth import login, logout
from django.http import HttpResponse
from django.db.models import F

def search_view(request):
    query = request.GET.get('s', '')
    if query:
        candidate = models.CustomUser.objects.filter(full_name__icontains=query)
        if candidate:
            context = {
                'candidates': candidate
            }
    else:
        return HttpResponse('Кандидаты не найдены')
    return render(request=request, template_name='customRegistration/candidates_list.html', context=context)

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
        form = forms.CustomLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/candidates_list/')
        
    else:
        form = forms.CustomLoginForm()
    return render(request=request, template_name='customRegistration/login.html', context={'form': form})

def auth_logout_view(request):
    logout(request)
    return redirect('/login/')

def candidates_list_view(request):
    candidates = models.CustomUser.objects.all().order_by('-id')
    paginator = Paginator(candidates, 3)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)

    context = {
        'candidates': page_obj
    }

    return render(request, 'customRegistration/candidates_list.html', context)

def candidate_detailed_view(request, id):
    if request.method == 'GET':
        candidate = get_object_or_404(models.CustomUser, id=id)
        views_candidate = request.session.get('viewed_candidate', [])

        if id not in views_candidate:
            candidate.views = F('views') + 1
            candidate.save()
            candidate.refresh_from_db
        views_candidate.append(id)
        request.session['viewed_candidate'] = views_candidate

        context = {
            'candidate': candidate
        }
    return render(request, template_name='customRegistration/candidate_detailed.html', context=context)
