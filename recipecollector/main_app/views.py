from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Recipe

def index(request):
  # return HttpResponse('<h1>Hello World! /ᐠ｡‸｡ᐟ\ﾉ</h1>')
  return render(request, 'index.html')

def about(request):
  # return HttpResponse('<h1>I am Katherine, the developer</h1>')
  return render(request, 'about.html')

# class Recipe:
#   def __init__(self, title, source, category):
#     self.title = title
#     self.source = source
#     self.category = category

# recipes = [
#   Recipe('The Best Banana Cake', 'https://www.spendwithpennies.com/banana-cake/', 'desert'),
#   Recipe('Italian Pistachio Cookie Recipe', 'https://foreignfork.com/pistachio-cookies/', 'desert'),
#   Recipe('Coconut Shrimp Curry', 'https://www.jocooks.com/recipes/coconut-shrimp-curry/', 'main')
# ]

def recipes_index(request):
  recipes = Recipe.objects.all()
  return render(request, 'recipes/index.html', {'recipes': recipes})

def recipes_show(request, recipe_id):
  recipe = Recipe.objects.get(id=recipe_id)
  return render(request, 'recipes/show.html', {'recipe': recipe})

class RecipeCreate(CreateView):
    # use the model Recipe
    model = Recipe
    # utilize all fields from the model Recipe
    # fields = '__all__'
    fields = ['title', 'source', 'category']
    # redirect upon successful creation
    success_url = '/recipes'

    def form_valid(self, form):
        # creating an object from the form
        self.object = form.save(commit=False)
        # adding a user to that object
        self.object.user = self.request.user
        # saving the object in the db
        self.object.save()
        # redirecting to the main index page
        return HttpResponseRedirect('/recipes')

class RecipeUpdate(UpdateView):
    # use the model Recipe
    model = Recipe
    fields = ['title', 'source', 'category']
    # now we use a function to determine if our form data is valid
    def form_valid(self, form):
        # commit=False is useful when we're getting data from a form
        # but we need to populate with some non-null data
        # saving with commit=False gets us a model object, then we can add our extra data and save
        self.object = form.save(commit=False)
        self.object.save()
        # pk is the primary key, aka the id of the object
        return HttpResponseRedirect('/recipes/' + str(self.object.pk))

class RecipeDelete(DeleteView):
    model = Recipe
    success_url = '/recipes'