# Generated by Django 4.1.2 on 2022-12-05 21:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0022_film_slug_serie_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='filmvisit',
            old_name='serie',
            new_name='film',
        ),
    ]
