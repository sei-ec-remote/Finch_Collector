from turtle import title
from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    source = models.CharField(max_length=250)
    category = models.CharField(max_length=100)