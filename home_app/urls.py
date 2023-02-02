from django.urls import path
from .views import HomeView, search_box, GenreFilterList, YearFilterList
urlpatterns = [
    path('', HomeView.as_view(), name='home-page'),
    path('search/', search_box, name='search-box'),
    path('genre/<str:genre>', GenreFilterList.as_view(), name='genre-filter-page'),
    path('year/<str:year>', YearFilterList.as_view(), name='year-filter-page')
]
