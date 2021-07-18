from rest_framework import serializers

from imdb.models import Movie, Genres

from django.contrib.auth import get_user_model


class MovieSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='movie_detail')
    author = serializers.SerializerMethodField(read_only=True)

    def get_author(self, obj):
        return obj.author.id

    class Meta:
        model = Movie
        fields = ('title', 'url', 'author', 'release_date', 'genre', 'duration', 'description', 'rating')


class GenreSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='genre_detail')

    class Meta:
        model = Genres
        fields = ('title', 'url')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        queryset = model.objects.all()
        fields = ('id', 'email', 'password', 'username', 'is_superuser')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', '')
        user = self.Meta.model(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.set_password(validated_data.pop('password', ''))
        return super().update(instance, validated_data)
