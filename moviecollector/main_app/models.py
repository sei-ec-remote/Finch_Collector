from django.db import models

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    description = models.CharField(max_length=700)
    year = models.IntegerField()

    def __str__(self):
        return self.name