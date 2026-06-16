from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm

urlpatterns = [
    path('movies_list/', views.MovieListView.as_view(), name='movies_list'),
    path('movie_detailed/<int:id>', views.MovieDetailedView.as_view(), name='movie_detailed'),
    path('movie/user_registration/', views.UserRegisterView.as_view(), name='registration'),
    path('movie/user_auth/', LoginView.as_view(template_name='cineboard/login.html', redirect_authenticated_user=True, form_class=AuthenticationForm, next_page='/movies_list/'), name='login'),
    path('movie/user_logout/', LogoutView.as_view(next_page='/movie/user_auth/'), name='logout'),
    path('movies_list/search/', views.MovieSearchView.as_view(), name='search'),
    path('movie/delete_movie/<int:id>', views.MovieDeleteView.as_view(), name='delete_movie'),
    path('movie/update_movie/<int:id>', views.MovieUpdateView.as_view(), name='update_movie'),
    path('movie/create_movie/', views.MovieCreateView.as_view(), name='create_movie'),
    path('movie/create_genre/', views.GenreCreateView.as_view(), name='create_genre'),
    path('movies_list/<int:id>', views.MoviesOfGenreView.as_view(), name='movies_of_genre'),
    path('movie/create_comment/<int:id>/', views.CreateCommentView.as_view(), name='create_comment'),
    path('movie/create_vip_place/', views.CreateVipPlace.as_view(), name='create_vip_place'),
    path('movie/reservation_vip_place/', views.ReservVipPlace.as_view(), name='reservation_vip_place'),
]