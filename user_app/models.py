from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class User(AbstractUser):
    email_active_code = models.CharField(max_length=100, verbose_name="Email activation code")
    saved_series = models.ManyToManyField('movie_app.Serie', related_name='saved_series', blank=True)
    saved_films = models.ManyToManyField('movie_app.Film', related_name='saved_series', blank=True)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.email
