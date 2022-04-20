from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .models import Movie

def index(request):
  return render(request, 'index.html')

def about(request):
  return render(request, 'about.html')

def movies_index(request):
    movies = Movie.objects.all()
    return render(request, 'movies/index.html', {'movies': movies})
