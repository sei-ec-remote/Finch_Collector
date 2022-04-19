from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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

class MovieCreate(CreateView):
    # use the model Movie
    model = Movie
    # utilize all fields from the model movie
    fields = '__all__'
    # redirect upon successful
    success_url = '/movies'

class MovieUpdate(UpdateView):
    # use the model Movie
    model = Movie
    # we need to define fields, but only use the right ones
    # that means, no changing or attempting to change the id
    fields = ['name', 'genre', 'description', 'year']

    # now we use a function to determine if our form data is valid
    def form_valid(self, form):
        # commit=False is useful when we're getting data from a form
        # but we need to populate with some non-null info
        # saving with commit=False gets us a model object, then we can add our extra data and save
        self.object = form.save(commit=False)
        self.object.save()
        # pk is the primary key AKA the ID of the object
        # go back to show page after movie is updated
        return HttpResponseRedirect('/movies/' + str(self.object.pk))

class MovieDelete(DeleteView):
    model = Movie
    success_url = '/movies'