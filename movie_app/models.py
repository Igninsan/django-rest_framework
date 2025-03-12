from django.db import models
from django.db.models import TextField, ForeignKey, IntegerField


class Director(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    duration = models.TimeField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name='director')

    def __str__(self):
        return self.title

    @property
    def rating(self):
        star_count = [i.stars for i in self.reviews.all()]
        return sum(star_count) / len(star_count)


STARS = (
    (star, '*' * star) for star in range(1, 6)
)

class Review(models.Model):
    text = TextField(null=True, blank=True)
    movie = ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    stars = IntegerField(choices=STARS, default=3)

    def __str__(self):
        return f'Отзыв на фильм: {self.movie.title}'

