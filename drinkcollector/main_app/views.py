from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Drink

def index(request):
    return render(request, 'index.html')

def drinks_index(request):
    drinks = Drink.objects.all()
    return render (request, 'drinks/index.html', {'drinks' : drinks})

def drinks_show(request, drink_id):
    drink = Drink.objects.get(id=drink_id)
    return render(request, 'drinks/show.html', {'drink' : drink})

class DrinkCreate(CreateView):
    # use the model Drink
    model = Drink
    # utilize all fields from the model drink
    fields = '__all__'
    # redirect upon successful creation
    success_url = '/drinks'

class DrinkUpdate(UpdateView):
    # use the model Drink
    model = Drink
    # define fields, but only use the right ones
    # no changing or attempting to change id
    fields = ['name', 'ingredients', 'description', 'method']

    # now we use a function to determine if our form data is valid
    def form_valid(self, form):
        # commit = false is useful when we're getting data from a form
        # but we need to populate with some non-null info
        # saving with commit=False gets us a model object, then we can add our extra data and save
        self.object = form.save(commit=False)
        self.object.save()
        # pk is the primary key, aka the id of the object
        return HttpResponseRedirect('/drinks/' + str(self.object.pk))

class DrinkDelete(DeleteView):
    model = Drink
    success_url = '/drinks'