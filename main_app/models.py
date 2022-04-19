from django.db import models

# This is the sql database model for Jewelry.  It defines the table.
class Jewelry(models.Model):
    type = models.CharField(max_length=100)
    metal = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    color = models.CharField(max_length=20)
    year = models.IntegerField()

    def __str__(self):
        return self.type