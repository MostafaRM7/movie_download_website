from django.db.models import Count
from django.views.generic import DetailView, ListView
from utils.tools import get_client_ip
from .models import Serie, Film, Part, Season, FilmByQuality, FilmVisit, SerieVisit, Genre, Date


class SerieComponent(DetailView):
    template_name = 'serie_download_page.html'
    model = Serie
    context_object_name = 'serie'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_serie = self.object
        context['seasons'] = Season.objects.filter(serie__slug=loaded_serie.slug).all()
        context['parts'] = Part.objects.filter(season__serie__slug=loaded_serie.slug).all()
        context['related_series'] = Serie.objects.filter(genre=loaded_serie.genre.first()).exclude(pk=loaded_serie.id)
        if self.request.user.is_authenticated:
            context['is_favorite'] = self.request.user.saved_series.filter(pk=loaded_serie.id).exists()
        user_ip = get_client_ip(self.request)
        user_id = None
        if self.request.user.is_authenticated:
            user_id = self.request.user.id

        has_been_visited = SerieVisit.objects.filter(ip__iexact=user_ip, serie_id=loaded_serie.id).exists()

        if not has_been_visited:
            new_visit = SerieVisit(ip=user_ip, user_id=user_id, serie_id=loaded_serie.id)
            new_visit.save()

        return context


class FilmComponent(DetailView):
    template_name = 'film_download_page.html'
    model = Film
    context_object_name = 'film'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_film = self.object
        context['film_qualities'] = FilmByQuality.objects.prefetch_related().filter(film__slug=loaded_film.slug).all()
        context['related_films'] = Film.objects.filter(genre=loaded_film.genre.first()).exclude(pk=loaded_film.id)
        if self.request.user.is_authenticated:
            context['is_favorite'] = self.request.user.saved_films.filter(pk=loaded_film.id).exists()

        user_ip = get_client_ip(self.request)
        user_id = None
        if self.request.user.is_authenticated:
            user_id = self.request.user.id

        has_been_visited = FilmVisit.objects.filter(ip__iexact=user_ip, film_id=loaded_film.id).exists()

        if not has_been_visited:
            new_visit = FilmVisit(ip=user_ip, user_id=user_id, film_id=loaded_film.id)
            new_visit.save()

        return context


class FilmList(ListView):
    template_name = 'films_page.html'
    model = Film
    context_object_name = 'films'
    ordering = ['-imdb']
    paginate_by = 6

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['most_visit'] = Film.objects.filter(is_active=True).annotate(
            visit_count=Count('filmvisit')).order_by('-visit_count')[:8]
        context['all_genres'] = Genre.objects.all()
        context['all_years'] = Date.objects.all()

        return context


class SerieList(ListView):
    template_name = 'series_page.html'
    model = Serie
    context_object_name = 'series'
    ordering = ['-imdb']
    paginate_by = 6

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['most_visit'] = Serie.objects.filter(is_active=True).annotate(
            visit_count=Count('serievisit')).order_by('-visit_count')[:8]
        context['all_genres'] = Genre.objects.all()
        context['all_years'] = Date.objects.all()

        return context
