from django.shortcuts import render
from .models import Album
# from django.http import HttpResponse

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