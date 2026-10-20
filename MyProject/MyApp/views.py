from django.shortcuts import get_object_or_404, redirect, render
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

def landing(request):
    movies = Movie.objects.all()

    context = {
        'total': movies.count(),
        'recent_movies': movies.order_by('-id')[:6],
        'top_rated': movies.order_by('-rating')[:6],
        'genres': movies.order_by('genre').values_list('genre', flat=True).distinct(),
    }
    return render(request, 'movieApp/landing.html', context)

def edit_movie(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movie_list')
    else:
        form = MovieForm(instance=movie)

    context = {
        'form': form
    }
    return render(request, 'movieApp/movie_form.html', context)

def delete_movie(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        movie.delete()
        return redirect('movie_list')

    context = {
        'movie': movie
    }
    return render(request, 'movieApp/movie_confirm_delete.html', context)