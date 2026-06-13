from . import views, forms
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('registration/', views.RegisterView.as_view(), name='registration'),
    path('login/', LoginView.as_view(template_name='customRegistration/login.html', redirect_authenticated_user=True, form_class=forms.CustomLoginForm, next_page='/candidates_list/'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('candidates_list/', views.CandidatesListView.as_view(), name='candidates_list'),
    path('candidates/search/', views.SearchView.as_view(), name='candidates_search'),
    path('candidates_list/<int:id>', views.CandidateDetailedView.as_view(), name='candidates_list_detailed'),
]