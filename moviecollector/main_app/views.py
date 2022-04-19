from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
  return render(request, 'index.html')

def about(request):
  return render(request, 'about.html')

def movies_index(request):
    return render(request, 'movies/index.html', {'movies': movies})


class Movie:
    def __init__(self, name, genre, description):
        self.name = name
        self.genre = genre
        self.description = description
    
movies = [
    Movie('Guardians of the Galaxy', 'action', 'very good'),
    Movie('The Shawshank Redemption', 'crime', 'very good very good'),
    Movie('The Dark Knight', 'action', 'very classic')
]