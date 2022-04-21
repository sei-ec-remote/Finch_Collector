from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  # return HttpResponse('<h1>Hello World! /ᐠ｡‸｡ᐟ\ﾉ</h1>')
  return render(request, 'index.html')

def about(request):
  # return HttpResponse('<h1>I am Katherine, the developer</h1>')
  return render(request, 'about.html')

class Recipe:
  def __init__(self, title, source, category):
    self.title = title
    self.source = source
    self.category = category

recipes = [
  Recipe('The Best Banana Cake', 'https://www.spendwithpennies.com/banana-cake/', 'desert'),
  Recipe('Italian Pistachio Cookie Recipe', 'https://foreignfork.com/pistachio-cookies/', 'desert'),
  Recipe('Coconut Shrimp Curry', 'https://www.jocooks.com/recipes/coconut-shrimp-curry/', 'main')
]

def recipes_index(request):
  return render(request, 'recipes/index.html', {'recipes': recipes})