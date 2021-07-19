from django.db import models

from django.urls import reverse_lazy

from django.conf import settings

from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType

from users.models import User


class Movie(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=False)
    release_date = models.DateField()
    genre = models.ForeignKey('Genres', null=True, on_delete=models.SET_NULL)
    duration = models.IntegerField()
    description = models.TextField(max_length=1000)
    rating = GenericRelation('Likes')

    class Meta:
        ordering = ['pk']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('movie', kwargs={'pk': self.pk})

    @property
    def total_likes(self):
        return self.rating.count()


class Genres(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('genres', kwargs={'genre_id': self.pk})


class Likes(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='rating')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
