from django.db import models

# Create your models here.
class Album(models.Model):
    artist = models.CharField(max_length=100)
    albumName = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    yearOfRelease = models.IntegerField()

    def __str__(self):
        return self.albumName


# a = Album(artist="", albumName='', genre='',yearOfRelease=)
# a.save()