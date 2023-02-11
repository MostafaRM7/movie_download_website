from django.db import models
from django.db.models import Model

from movie_app.models import Serie, Film


# Create your models here.


class Slider(Model):
    number_1 = models.OneToOneField(Film, on_delete=models.CASCADE, related_name='one')
    number_2 = models.OneToOneField(Serie, on_delete=models.CASCADE, related_name='two')
    number_3 = models.OneToOneField(Serie, on_delete=models.CASCADE, related_name='three')
    number_4 = models.OneToOneField(Serie, on_delete=models.CASCADE, related_name='four')
    number_5 = models.OneToOneField(Film, on_delete=models.CASCADE, related_name='five')
    is_active = models.BooleanField()

    def save(self, *args, **kwargs):
        if self.is_active:
            try:
                temp = Slider.objects.get(is_active=True)
                if self != temp:
                    temp.is_active = False
                    temp.save()
            except Slider.DoesNotExist:
                pass
        super(Slider, self).save(*args, **kwargs)

    def __str__(self):
        string = f'({self.number_1.name}-{self.number_2.name}-{self.number_3.name}-{self.number_4.name}-{self.number_5.name})'
        if self.is_active:
            string += ' <ACTIVE> '
        return string


class HomePageSlider(Model):
    recent_films_slider_1 = models.ManyToManyField(Film, related_name='recent_films')
    recent_series_slider_2 = models.ManyToManyField(Serie, related_name='recent_series')
    is_active = models.BooleanField()

    def __str__(self):
        result = ''
        for film in self.recent_films_slider_1.all():
            result += film.name + ' - '
        for serie in self.recent_series_slider_2.all():
            result += serie.name + ' - '
        return result

    def save(self, *args, **kwargs):
        if self.is_active:
            try:
                temp = HomePageSlider.objects.get(is_active=True)
                if self != temp:
                    temp.is_active = False
                    temp.save()
            except HomePageSlider.DoesNotExist:
                pass
        super(HomePageSlider, self).save(*args, **kwargs)


class SiteSetting(Model):
    site_name = models.CharField(max_length=75)
    site_logo = models.FileField(upload_to='uploads/site_logo')
    favicon = models.FileField(upload_to='uploads/favicon')
    telegram = models.URLField()
    email = models.EmailField()
    is_active = models.BooleanField()

    def save(self, *args, **kwargs):
        if self.is_active:
            try:
                temp = SiteSetting.objects.get(is_active=True)
                if self != temp:
                    temp.is_active = False
                    temp.save()
            except SiteSetting.DoesNotExist:
                pass
        super(SiteSetting, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.site_name} - {self.telegram} - {self.email}'
