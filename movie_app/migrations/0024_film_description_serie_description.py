# Generated by Django 4.1.2 on 2022-12-06 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0023_rename_serie_filmvisit_film'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='serie',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
