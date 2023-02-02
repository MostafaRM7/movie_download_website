from django.contrib import admin
from . import models
# Register your models here.


admin.site.register(models.Film)
admin.site.register(models.Part)
admin.site.register(models.Serie)
admin.site.register(models.Season)
admin.site.register(models.Quality)
admin.site.register(models.Genre)
admin.site.register(models.FilmByQuality)
admin.site.register(models.Date)
admin.site.register(models.Language)
admin.site.register(models.Country)
admin.site.register(models.FilmVisit)
admin.site.register(models.SerieVisit)


