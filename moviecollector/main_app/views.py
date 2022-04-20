from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.http import HttpResponse
# Create your views here.

from .models import Movie

def index(request):
  return render(request, 'index.html')

def about(request):
  return render(request, 'about.html')

def movies_index(request):
    movies = Movie.objects.all()
    return render(request, 'movies/index.html', {'movies': movies})
  
def movies_show(request, movie_id):
        movie = Movie.objects.get(id=movie_id)
        return render(request, 'movies/show.html', {'movie': movie})

class MovieCreate(CreateView):
  model = Movie
  fields = '__all__'
  success_url = '/movies'

class MovieUpdate(UpdateView):
  model = Movie
  fields = ['name', 'genre', 'description']

  def form_valid(self, form):
    self.object = form.save(commit=False)
    self.object.save()
    return HttpResponseRedirect('/movies/' + str(self.object.pk))

class MovieDelete(DeleteView):
  model = Movie
  success_url = '/movies'

# class Movie:
#     def __init__(self, name, genre, description):
#         self.name = name
#         self.genre = genre
#         self.description = description
    
# movies = [
#     Movie('Guardians of the Galaxy', 'action', 'very good'),
#     Movie('The Shawshank Redemption', 'crime', 'very good very good'),
#     Movie('The Dark Knight', 'action', 'very classic')
# ]