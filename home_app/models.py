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


class RecentlyUpdated(Model):
    series = models.ManyToManyField(Serie, related_name='lately_updated')
    is_active = models.BooleanField()

    def __str__(self):
        all_series = ''
        for serie in self.series.all():
            all_series += serie.name + ' - '
        return all_series

    def save(self, *args, **kwargs):
        if self.is_active:
            try:
                temp = RecentlyUpdated.objects.get(is_active=True)
                if self != temp:
                    temp.is_active = False
                    temp.save()
            except RecentlyUpdated.DoesNotExist:
                pass
        super(RecentlyUpdated, self).save(*args, **kwargs)


class SiteSettings(Model):
    telegram_id = models.CharField(max_length=75)

