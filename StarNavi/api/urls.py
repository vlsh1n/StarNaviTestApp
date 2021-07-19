from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter

from .views import GenreListView, GenreDetailView, MovieViewSet, UserViewSet

router = DefaultRouter()
router.register('users', UserViewSet, basename='users')


movie_list = MovieViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
movie_detail = MovieViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
movie_like = MovieViewSet.as_view({
    'post': 'like',
    'get': 'fans'
})
movie_dislike = MovieViewSet.as_view({
    'post': 'unlike',
    'get': 'fans'
})


urlpatterns = [
    path('movies/', movie_list),
    path('movies/<int:pk>/', movie_detail, name='movie_detail'),
    path('movies/<int:pk>/like/', movie_like, name='movie_like'),
    path('movies/<int:pk>/dislike/', movie_dislike, name='movie_dislike'),
    path('genres/', GenreListView.as_view()),
    path('genres/<int:pk>', GenreDetailView.as_view(), name='genre_detail')
]
urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns += router.urls
