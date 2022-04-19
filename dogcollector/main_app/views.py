from django.shortcuts import render
from django.http import HttpResponse
from .models import Dog

# Create your views here.


def index(request):
    return HttpResponse('<h1>Hello World! /ᐠ｡‸｡ᐟ\ﾉ</h1>')


def about(request):
    return HttpResponse('<h1>testing view page</h1>')


def dogs_index(request):
    dogs = Dog.objects.all()
    return render(request, 'dogs/index.html', {'dogs': dogs})


def dogs_show(request, dog_id):
    dog = Dog.objects.get(id=dog_id)
    return render(request, 'dogs/show.html', {'dog': dog})
