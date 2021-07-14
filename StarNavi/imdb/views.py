from django.shortcuts import get_object_or_404

# Create your views here.
from django.views.generic import ListView, DetailView

from .models import Movie, Genres


class MainPage(ListView):
    model = Movie
    template_name = 'imdb/index.html'
    context_object_name = 'movies'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(MainPage, self).get_context_data()
        context['title'] = 'Main Page | StarNavi'
        context['genres'] = Genres.objects.all()
        return context


class MovieDetail(DetailView):
    model = Movie
    template_name = 'imdb/movie.html'
    context_object_name = 'movie'

    def get_context_data(self, **kwargs):
        context = super(MovieDetail, self).get_context_data()
        context['title'] = f'{self.kwargs["title"]} | StarNavi'


class MoviesByGenre(ListView):
    template_name = 'imdb/movies_by_genre.html'

    def get_queryset(self):
        self.genre = get_object_or_404(Genres, title=self.kwargs['genre'])
        return Movie.objects.filter(genre=self.genre)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(MoviesByGenre, self).get_context_data()
        context['genre'] = self.genre
        return context
