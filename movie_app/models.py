from django.db import models
from django.db.models import Model, QuerySet
from django.urls import reverse
from django.utils.text import slugify

from user_app.models import User


# TODO add rating
class Country(Model):
    country = models.CharField(max_length=75)

    def __str__(self):
        return self.country


class Language(Model):
    lang = models.CharField(max_length=75)

    def __str__(self):
        return self.lang


class Date(Model):
    date = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.date.year}"

    def get_absolute_url(self):
        return reverse('year-filter-page', args=[self.date.year])


class Genre(Model):
    genre = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse('genre-filter-page', args=[self.genre])

    def __str__(self):
        return self.genre


class Quality(Model):
    quality = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.quality


class Serie(Model):
    name = models.CharField(max_length=300)
    imdb = models.FloatField(null=True, blank=True)
    director = models.CharField(max_length=50)
    banner = models.FileField(upload_to='uploads/banners')
    release_date = models.ForeignKey(to=Date, on_delete=models.CASCADE, related_name='release')
    end_date = models.ForeignKey(to=Date, on_delete=models.CASCADE, related_name='end')
    genre = models.ManyToManyField(to=Genre, related_name='serie_genre')
    cast = models.CharField(max_length=200, null=True, blank=True)
    background = models.ImageField(upload_to='uploads/backgrounds', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    description = models.TextField(null=True)
    country = models.ForeignKey(to=Country, null=True, blank=True, on_delete=models.CASCADE)
    lang = models.ForeignKey(to=Language, null=True, blank=True, on_delete=models.CASCADE)
    slug = models.SlugField(db_index=True, blank=True)

    def get_absolute_url(self):
        return reverse('serie-page', args=[self.slug])

    def __str__(self):
        return f'{self.name}-{self.release_date}/{self.end_date}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Serie, self).save(*args, **kwargs)


class Season(Model):
    serie = models.ForeignKey(to=Serie, on_delete=models.CASCADE)
    parts_count = models.IntegerField()
    part_avg_length = models.IntegerField()
    number = models.IntegerField()
    quality = models.ForeignKey(to=Quality, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.serie} - {self.quality} - S{self.number} "


class Part(Model):
    file = models.FileField(upload_to='uploads/series')
    season = models.ForeignKey(to=Season, on_delete=models.CASCADE)
    number = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.season} E{self.number}"


class Film(Model):
    name = models.CharField(max_length=300)
    length = models.IntegerField()
    imdb = models.FloatField(null=True, blank=True)
    director = models.CharField(max_length=50)
    banner = models.ImageField(upload_to='uploads/banners')
    release_date = models.ForeignKey(to=Date, on_delete=models.CASCADE)
    genre = models.ManyToManyField(to=Genre, related_name='film_genre')
    background = models.ImageField(upload_to='uploads/backgrounds', blank=True, null=True)
    cast = models.CharField(max_length=200, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    description = models.TextField(null=True)
    country = models.ForeignKey(to=Country, null=True, blank=True, on_delete=models.CASCADE)
    lang = models.ForeignKey(to=Language, null=True, blank=True, on_delete=models.CASCADE)
    slug = models.SlugField(db_index=True, blank=True)

    def get_absolute_url(self):
        return reverse('film-page', args=[self.slug])

    def __str__(self):
        return f'{self.name} - {self.release_date}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Film, self).save(*args, **kwargs)


class FilmByQuality(Model):
    film = models.ForeignKey(to=Film, on_delete=models.CASCADE)
    file = models.FileField(upload_to="uploads/films")
    quality = models.ForeignKey(to=Quality, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.film} - {self.quality}"


class SerieVisit(Model):
    serie = models.ForeignKey(to=Serie, on_delete=models.CASCADE)
    ip = models.CharField(max_length=30)
    user = models.ForeignKey(to='user_app.User', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        if self.user is not None:
            name = f'{self.serie} - {self.ip} - {self.user.username}'
        else:
            name = f'{self.serie} - {self.ip}'

        return name


class FilmVisit(Model):
    film = models.ForeignKey(to=Film, on_delete=models.CASCADE)
    ip = models.CharField(max_length=30)
    user = models.ForeignKey(to='user_app.User', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        name = ''
        if self.user is not None:
            name = f'{self.film} - {self.ip} - {self.user.username}'
        elif self.user is None:
            name = f'{self.film} - {self.ip}'

        return name






