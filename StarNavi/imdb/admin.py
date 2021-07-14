from django.contrib import admin

from .models import Movie, Genres

# Register your models here.


class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'genre', 'rating')
    list_display_links = ('id', 'title')
    list_filter = ('genre',)
    save_on_top = True
    search_fields = ['title']


admin.site.register(Movie, MovieAdmin)


class GenresAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    save_on_top = True


admin.site.register(Genres, GenresAdmin)
