from django.db import models

class Pizza(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    toppings = models.CharField(max_length=200)
    def __str__(self):
        return self.name