from django.shortcuts import render
from .models import Album 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
  return render(request, 'index.html')

def about(request):
  return render(request, 'about.html')


# class Album:
#     def __init__(self,artist,albumName,genre,yearOfRelease):
#         self.artist = artist
#         self.albumName = albumName
#         self.genre = genre
#         self.yearOfRelease = yearOfRelease

# albums = [
#     Album('The Weekend', 'Dawn FM', 'R&B', 2022),
#     Album('TYLER THE CREATOR', 'IGOR', 'Hip-hop', 2019),
#     Album('Dua Lipa', 'Future Nostalgia', 'Pop', 2020)
# ]


def albums_index(request):
    albums = Album.objects.all()
    return render(request, 'albums/index.html', {'albums':albums})

def albums_show(request, album_id):
    album = Album.objects.get(id=album_id)
    return render(request, 'albums/show.html', {'album':album})

class AlbumCreate(CreateView):
    model = Album
    fields = '__all__'
    success_url = '/albums'

class AlbumUpdate(UpdateView):
    model=Album
    fields = ['artist', 'albumName', 'genre', 'yearOfRelease']

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return HttpResponseRedirect('/albums/' + str(self.object.pk))

class AlbumDelete(DeleteView):
    model = Album
    success_url = '/albums'

