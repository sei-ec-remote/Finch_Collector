from django.shortcuts import render
# from django.http import HttpResponse
from .models import Dog
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect

# Create your views here.

def index(request):
  return render(request, 'index.html')

def about(request):
  return render(request, 'about.html')


# class Dog:
#     def __init__(self, name, breed, description, age):
#         self.name = name
#         self.breed = breed
#         self.description = description
#         self.age = age

# dogs = [
#     Dog('Manny', 'german shepard', 'spunky old soul', 13),
#     Dog('Maria', 'pitbull', 'the sweetest dog you\'ve ever met', 3),
#     Dog('Wolf', 'husky', '3 paws and a heart of gold', 6)
# ]

def dogs_index(request):
        dogs = Dog.objects.all()
        return render(request, 'dogs/index.html', { 'dogs': dogs })

def dogs_show(request, dog_id):
    dog = Dog.objects.get(id=dog_id)
    return render(request, 'dogs/show.html', {'dog': dog})


class DogCreate(CreateView):
  model = Dog
  fields = '__all__'
  success_url = '/cats'

class CatUpdate(UpdateView):
  model = Dog
  fields = ['name', 'breed', 'description', 'age']

  def form_valid(self, form):
    self.object = form.save(commit=False)
    self.object.save()
    return HttpResponseRedirect('/dogs/' + str(self.object.pk))

class DogDelete(DeleteView):
  model = Dog
  success_url = '/dogs'