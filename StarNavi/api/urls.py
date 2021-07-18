from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter

from .views import MovieListView, GenreListView, MovieDetailView, GenreDetailView, UserViewSet

router = DefaultRouter()
router.register('users', UserViewSet, basename='users')


urlpatterns = [
    path('movies/', MovieListView.as_view()),
    path('genres/', GenreListView.as_view()),
    path('movies/<int:pk>', MovieDetailView.as_view(), name='movie_detail'),
    path('genres/<int:pk>', GenreDetailView.as_view(), name='genre_detail')
]
urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns += router.urls
