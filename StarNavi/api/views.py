from rest_framework import views, status

from rest_framework.response import Response

from imdb.models import Movie, Genres

from .serializers import MovieSerializer, GenreSerializer

from rest_framework.mixins import ListModelMixin, CreateModelMixin

from rest_framework.generics import GenericAPIView, RetrieveUpdateDestroyAPIView


class MovieListView(views.APIView):
    def get(self, request, format=None):
        movies = Movie.objects.all()
        context = {'request': request}
        serializer = MovieSerializer(movies, many=True, context=context)
        return Response(serializer.data)

    def post(self, request, format=None):
        context = {'request': request}
        serializer = MovieSerializer(data=request.data, context=context)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GenreListView(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = Genres.objects.all()
    serializer_class = GenreSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class MovieDetailView(views.APIView):
    def get_object(self, pk):
        try:
            return Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        movie = self.get_object(pk)
        context = {'request': request}
        serializer = MovieSerializer(movie, context=context)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        movie = self.get_object(pk)
        context = {'request': request}
        serializer = MovieSerializer(movie, context=context, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        movie = self.get_object(pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class GenreDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Genres.objects.all()
    serializer_class = GenreSerializer
