from django.urls import path

from views import MainPage, Movie

urlpatterns = [
    path('', MainPage.as_view, name='home'),
    path('movie/<pk:number>', Movie.as_view, name='movie'),
]