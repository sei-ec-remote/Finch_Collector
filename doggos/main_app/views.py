from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here ...

# Index
def index(request):
    # return HttpResponse('<h1> Woof! υ´• ﻌ •`υ </h1>')
    return render(request, 'index.html')

# About
def about(request):
    return render(request, 'about.html')

# Class Constructor for Dogs (dummy data)
class Dog:
    def __init__(self, name, breed, description, age):
        self.name = name
        self.breed = breed
        self.description = description
        self.age = age

dogs = [
    Dog('Chibi', 'Shiba Inu', 'Spoiled', 6),
    Dog('Yuki', 'Aussie', 'Zoomies', 4),
    Dog('Loki', 'Aussie', 'Gudboi', 5)
]

def dogs_index(request):
    return render(request, 'dogs/index.html', {'dogs': dogs})
