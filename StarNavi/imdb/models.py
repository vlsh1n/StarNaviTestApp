from django.db import models

from django.urls import reverse_lazy

from users.models import User


class Movie(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=False)
    release_date = models.DateField()
    genre = models.ForeignKey('Genres', null=True, on_delete=models.SET_NULL)
    duration = models.IntegerField()
    description = models.TextField(max_length=1000)
    rating = models.PositiveIntegerField()

    class Meta:
        ordering = ['rating']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('movie', kwargs={'pk': self.pk})


class Genres(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('genres', kwargs={'genre_id': self.pk})
