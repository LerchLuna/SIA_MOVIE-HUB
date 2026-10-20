from django.shortcuts import redirect, render
from .models import Movie
from .forms import MovieForm
# Create your views here.

def movie_list(request):
    movies = Movie.objects.all()

    context = {
        'movies': movies
    }
    return render(request, 'movieApp/movie_list.html', context)

def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movie_list')
    else:
        form = MovieForm()

    context = {
        'form': form
    }
    return render(request, 'movieApp/movie_form.html', context)
