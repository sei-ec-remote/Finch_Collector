from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from .models import Song
# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')


# class Song:
#     def __init__(self, title, artist, genre, run_time):
#         self.title = title
#         self.artist = artist
#         self.genre = genre
#         self.run_time = run_time


# songs = [
#     Song('Need To Know', 'Doja Cat', 'Pop/Rap', 3),
#     Song('Wolves', 'Ye', 'Rap', 5),
#     Song('Selfish', 'Madison Beer', 'Pop', 3)
# ]

def songs_index(request):
    songs = Song.objects.all()
    return render(request, 'songs/index.html', {'songs': songs})

def songs_show(request, song_id):
    song = Song.objects.get(id=song_id)
    return render(request, 'songs/show.html', { 'song': song })

class SongCreate(CreateView):
    model = Song
    fields = '__all__'
    success_url = '/songs'

class SongUpdate(UpdateView):
    model = Song
    fields = ['title', 'artist', 'genre', 'run_time']

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return HttpResponseRedirect('/songs/' + str(self.object.pk))

class SongDelete(DeleteView):
    model = Song
    success_url = '/songs'