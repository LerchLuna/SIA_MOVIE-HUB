from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'type', 'genre', 'release_year', 'status', 'rating', 'description']

    widgets = {
        'title': forms.TextInput(attrs={'class': 'form-control'}),
        'type': forms.TextInput(attrs={'class': 'form-control'}),
        'genre': forms.TextInput(attrs={'class': 'form-control'}),
        'release_year': forms.NumberInput(attrs={'class': 'form-control'}),
        'status': forms.TextInput(attrs={'class': 'form-control'}),
        'rating': forms.NumberInput(attrs={'class': 'form-control'}),
        'description': forms.Textarea(attrs={'class': 'form-control'}),
    }    