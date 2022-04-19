from django.shortcuts import render
# from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Dog

# Create your views here ...

# Index
def index(request):
    # return HttpResponse('<h1> Woof! υ´• ﻌ •`υ </h1>')
    return render(request, 'index.html')

# About
def about(request):
    return render(request, 'about.html')

# Class Constructor for Dogs (dummy data)
# class Dog:
#     def __init__(self, name, breed, description, age):
#         self.name = name
#         self.breed = breed
#         self.description = description
#         self.age = age

# dogs = [
#     Dog('Chibi', 'Shiba Inu', 'Spoiled', 6),
#     Dog('Yuki', 'Aussie', 'Zoomies', 4),
#     Dog('Loki', 'Aussie', 'Gudboi', 5)
# ]

def dogs_index(request):
    dogs = Dog.objects.all()
    return render(request, 'dogs/index.html', {'dogs': dogs})

def dogs_show(request, dog_id):
    dog = Dog.objects.get(id=dog_id)
    return render(request, 'dogs/show.html', {'dog': dog})

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect

class DogCreate(CreateView):
  model = Dog
  fields = '__all__'
  success_url = '/dogs'

class DogUpdate(UpdateView):
  model = Dog
  fields = ['name', 'breed', 'description', 'age']

  def form_valid(self, form):
    self.object = form.save(commit=False)
    self.object.save()
    return HttpResponseRedirect('/dogs/' + str(self.object.pk))

class DogDelete(DeleteView):
  model = Dog
  success_url = '/dogs'