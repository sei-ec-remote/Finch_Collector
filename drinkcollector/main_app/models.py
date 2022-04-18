from django.db import models

# Create your models here.
class Drink(models.Model):
    # this is where we set up our columns and data types
    # similar to our mongoose schemas/models
    # we set the key with its name then tell what type of data to expect
    name = models.CharField(max_length=100)
    ingredients = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    method = models.CharField(max_length=100)

# this double underscore(dunder) method controls what happens when we print one of these objects
    def __str__(self):
        return self.name