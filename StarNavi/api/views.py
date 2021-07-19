from django.contrib.auth import get_user_model

from rest_framework.permissions import IsAdminUser

from rest_framework import views, status

from rest_framework.response import Response

from rest_framework.viewsets import ModelViewSet

from imdb.models import Movie, Genres

from .serializers import MovieSerializer, GenreSerializer, UserSerializer

from rest_framework.mixins import ListModelMixin, CreateModelMixin

from rest_framework.generics import GenericAPIView, RetrieveUpdateDestroyAPIView

from .permissions import IsAuthorOrReadOnly

from.mixins import LikesMixin


class GenreListView(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = Genres.objects.all()
    serializer_class = GenreSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class GenreDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Genres.objects.all()
    serializer_class = GenreSerializer


class UserViewSet(ModelViewSet):
    model = get_user_model()
    queryset = model.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser, )


class MovieViewSet(LikesMixin, ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (IsAuthorOrReadOnly, )

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)
