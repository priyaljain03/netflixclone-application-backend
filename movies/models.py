from distutils.command.upload import upload
from email.policy import default
from random import choices
from django.db import models

# Create your models here.
GENRE_CHOICES = (('action', 'Action'),
                 ('comedy', 'Comedy'),
                 ('romance', 'Romance'),
                 ('documentary', 'Documentary'),
                 ('fantasy', 'Fantasy'),
                 ('horror', 'Horror'),
                 ('mystery', 'Mystery'),
                 ('thriller', 'Thriller'),
                 ('crime', 'Crime'),
                 ('sci-fi', 'Sci-Fi'))

TYPE_CHOICES = (('seasonal', 'Seasonal'),
                ('single', 'Single'))

AGE_CHOICES = (('all', 'All'),
               ('kids', 'Kids'))


def upload_to(instance, filename):
    return 'flyers/{filename}'.format(filename=filename)


class Movie(models.Model):
    title = models.CharField(max_length=225)
    description = models.TextField(blank=True, null=True)
    genre = models.CharField(max_length=20, choices=GENRE_CHOICES, default=1)
    rating = models.IntegerField()
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default=1)
    created = models.DateTimeField(auto_now_add=True)
    flyer = models.ImageField(upload_to=upload_to, default='GOT.jfif')
    age_limit = models.CharField(max_length=10, choices=AGE_CHOICES, default=1)
    isNetflixOriginals = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Video(models.Model):
    title = models.CharField(max_length=225)
    description = models.TextField(max_length=500)
    movie = models.ForeignKey(
        Movie, blank=False, null=False, on_delete=models.CASCADE, related_name="movie",default="1")
    videofile = models.FileField(upload_to='movies', default='video1.mp4')

    def __str__(self):
        return self.movie.title + '-' + self.title
