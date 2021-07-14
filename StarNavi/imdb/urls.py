from django.urls import path

from .views import MainPage, MovieDetail, MoviesByGenre

urlpatterns = [
    path('', MainPage.as_view(), name='home'),
    path('genres/<int:genre_id>', MoviesByGenre.as_view(), name='genres'),
    path('movie/<int:pk>', MovieDetail.as_view(), name='movie'),
]
