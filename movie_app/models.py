from django.db import models
from django.db.models import TextField, ForeignKey


class Director(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    duration = models.TimeField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Review(models.Model):
    text = TextField(null=True, blank=True)
    movie = ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return f'Отзыв на фильм: {self.movie.title}'