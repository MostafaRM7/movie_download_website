# Generated by Django 4.1.1 on 2022-11-05 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0010_remove_serie_genre_serie_genre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='film',
            name='file',
        ),
        migrations.RemoveField(
            model_name='film',
            name='quality',
        ),
        migrations.CreateModel(
            name='FilmByQuality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='uploads/films')),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie_app.film')),
                ('quality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie_app.quality')),
            ],
        ),
    ]
