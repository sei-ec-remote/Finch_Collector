from turtle import title
from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    source = models.CharField(max_length=250)
    category = models.CharField(max_length=100)

    # this double underscore(dunder) method controls what happens when we print one of these objects
    def __str__(self):
        return self.title

    