from django.urls import path
from . import views

urlpatterns = [
    path('tours/', views.TourListView.as_view(), name="tour_list"),
    path('tours/search/', views.SearchView.as_view(), name='tours_search'),
    path('tours/<int:id>', views.TourListDetailedView.as_view(), name='tour_detailed'),
]