from rest_framework import serializers

from imdb.models import Movie, Genres


class MovieSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='movie_detail')

    class Meta:
        model = Movie
        fields = ('title', 'url', 'release_date', 'genre', 'duration', 'description', 'rating')


class GenreSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='genre_detail')

    class Meta:
        model = Genres
        fields = ('title', 'url')
