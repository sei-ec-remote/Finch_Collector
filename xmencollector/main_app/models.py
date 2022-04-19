from django.db import models

# Create your models here.
class Issue(models.Model):
    number = models.IntegerField()
    year = models.CharField(max_length=4)
    cover = models.CharField(max_length=10)
    writer = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)

# Defines what will be displayed when the object is passed to a print statement.
def __str__(self):
    return self.name
