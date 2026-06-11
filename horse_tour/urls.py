from django.urls import path
from . import views

urlpatterns = [
    path('tours/', views.tour_list_view, name="tour_list"),
    path('tours/search/', views.search_view, name='tours_search'),
    path('tours/<int:id>', views.tour_list_detailed_view, name='tour_detailed'),
]