# Generated by Django 4.1.2 on 2022-11-30 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0016_releasedate_remove_film_release_date_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ReleaseDate',
            new_name='Date',
        ),
        migrations.AddField(
            model_name='serie',
            name='end_date',
            field=models.ManyToManyField(related_name='serie_end_date', to='movie_app.date'),
        ),
    ]
