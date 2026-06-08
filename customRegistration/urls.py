from . import views
from django.urls import path

urlpatterns = [
    path('registration/', views.register_view, name='registration'),
    path('login/', views.auth_login_view, name='login'),
    path('logout/', views.auth_logout_view, name='logout'),
    path('candidates_list/', views.candidates_list_view, name='candidates_list')
]