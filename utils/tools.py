from django.db.models import QuerySet

from movie_app.models import Film


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

