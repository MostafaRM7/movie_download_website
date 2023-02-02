from django.urls import path

from .views import SerieComponent, FilmComponent, FilmList, SerieList

urlpatterns = [
    path('series/<slug:slug>', SerieComponent.as_view(), name="serie-page"),
    path('films/<slug:slug>', FilmComponent.as_view(), name="film-page"),
    path('films/', FilmList.as_view(), name='film-list-page'),
    path('series/', SerieList.as_view(), name='serie-list-page')
]
