from django.db import models

# Create your models here.
from django.urls import reverse_lazy


class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_date = models.DateField()
    genre = models.ForeignKey('Genres', null=True, on_delete=models.SET_NULL)
    duration = models.IntegerField()
    description = models.TextField(max_length=1000)
    rating = models.IntegerField()

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
