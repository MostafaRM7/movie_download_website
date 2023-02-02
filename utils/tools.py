from django.db.models import QuerySet

from movie_app.models import Film, Movie


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def related_finder(movie):
    related = []
    for film in Film.objects.all():
        for genre in film.genre.all():
            if genre in movie.genre.all():
                related.append(film)
                continue
    return related


class MovieQuerySet(QuerySet):
    @staticmethod
    def get_movies_queryset(fqs, sqs):
        result = []
        for film in fqs:
            result.append(Movie(film=film))
        for serie in sqs:
            result.append(Movie(serie=serie))
        return QuerySet(result)
