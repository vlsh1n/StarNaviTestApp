from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import MovieListView, GenreListView, MovieDetailView, GenreDetailView


urlpatterns = [
    path('movies/', MovieListView.as_view()),
    path('genres/', GenreListView.as_view()),
    path('movies/<int:pk>', MovieDetailView.as_view(), name='movie_detail'),
    path('genres/<int:pk>', GenreDetailView.as_view(), name='genre_detail')
]
urlpatterns = format_suffix_patterns(urlpatterns)
