from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Drink

def index(request):
  return render(request, 'index.html')

def drinks_index(request):
    drinks = Drink.objects.all()
    return render (request, 'drinks/index.html', {'drinks' : drinks})