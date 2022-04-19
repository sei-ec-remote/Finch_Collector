from django.shortcuts import render
# from django.http import HttpResponse
from .models import Movie

# Create your views here.
def index(request):
    return render(request, 'index.html')

# About page that describes the app
def about(request):
    return render(request, 'about.html')

def movies_index(request):
    movies = Movie.objects.all()
    return render(request, 'movies/index.html', {'movies': movies})

def movies_show(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request, 'movies/show.html', {'movie': movie})