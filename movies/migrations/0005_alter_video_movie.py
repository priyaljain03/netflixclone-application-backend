# Generated by Django 4.0.1 on 2022-02-18 19:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_movie_isnetflixoriginals'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='movie',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='movie', to='movies.movie'),
        ),
    ]