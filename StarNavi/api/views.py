from rest_framework import views, status

from rest_framework.response import Response

from imdb.models import Movie, Genres

from .serializers import MovieSerializer, GenreSerializer


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


class GenreListView(views.APIView):
    def get(self, request, format=None):
        genres = Genres.objects.all()
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
