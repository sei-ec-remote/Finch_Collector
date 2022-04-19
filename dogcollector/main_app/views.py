from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
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


class DogCreate(CreateView):
    model = Dog
    # utilize all fields from the model dog
    fields = '__all__'
    # redirect upon successful creation
    success_url = '/dogs'

    def form_valid(self, form):
        # creating an object from the form
        self.object = form.save(commit=False)
    # adding a user to that object
        self.object.user = self.request.user
    # saving object in the db
        self.object.save()
    # redirecting to the main index page
        return HttpResponseRedirect('/dogs')


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

    # user profile view


def profile(request, username):
    user = User.objects.get(username=username)
    dogs = Dog.objects.filter(user=user)
    return render(request, 'profile.html', {'username': username, 'dogs': dogs})
