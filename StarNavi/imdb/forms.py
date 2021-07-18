from django import forms

from .models import Movie


class AddMovieForm(forms.ModelForm):
    title = forms.CharField(label='Title', widget=forms.TextInput(attrs={'class': 'form-control'})),
    genre = forms.ChoiceField(label='Genre', widget=forms.Select(attrs={'class': 'form-control'})),
    release_date = forms.DateField(label='Release Date', widget=forms.SelectDateWidget(attrs={'class': 'form-control'})),
    description = forms.CharField(label='Description', widget=forms.Textarea(attrs={'class': 'form-control'})),
    duration = forms.IntegerField(label='Duration', widget=forms.NumberInput(attrs={'class': 'form-control'})),

    class Meta:
        model = Movie
        fields = ('title', 'genre', 'release_date', 'description', 'duration')
