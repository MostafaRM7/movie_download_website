from django.db import models
from django.db.models import Model

from movie_app.models import Serie, Film


# Create your models here.


class Slider(Model):
    number_1 = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='one', unique=True)
    number_2 = models.ForeignKey(Serie, on_delete=models.CASCADE, related_name='two', unique=True)
    number_3 = models.ForeignKey(Serie, on_delete=models.CASCADE, related_name='three', unique=True)
    number_4 = models.ForeignKey(Serie, on_delete=models.CASCADE, related_name='four', unique=True)
    number_5 = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='five', unique=True)
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
