from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Jewelry

# Used for Testing - Index view
def index(request):
    return HttpResponse('<h1>Hello World! /ᐠ｡‸｡ᐟ\ﾉ</h1>')

# About.html page
def about(request):
    return render(request, 'about.html')

# Render the Home index.html page
def index(request):
  return render(request, 'index.html')

#  Render the actual jewelry index page showing all jewels
def jewels_index(request):
    jewels = Jewelry.objects.all()
    return render(request, 'jewels/index.html', {'jewels': jewels})

# Show one piece of jewelry
def jewels_show(request, jewel_id):
        jewel = Jewelry.objects.get(id=jewel_id)
        return render(request, 'jewels/show.html', {'jewel': jewel})

# Use all the fields of our Jewelry model.  
# This is for Jewelry Creation.
# Redirect upon successful creation
class JewelCreate(CreateView):
  model = Jewelry
  fields = '__all__'
  success_url = '/jewels'

# This is for Jewelry Updating.  Use the Jewelry fields.
class JewelUpdate(UpdateView):
  model = Jewelry
  fields = ['type', 'metal', 'description', 'color', 'year']

  # python and postgresql 
  # Now we use a function to determin if a form is valid
  # We do not commit the form to the database on the form.save.
  def form_valid(self, form):
    self.object = form.save(commit=False)
    self.object.save()
    # pk is the primary key aka id of the object
    # Aftef the form redirect to the /jewels page
    return HttpResponseRedirect('/jewels/' + str(self.object.pk))

# Delete a piece of jewelry.  In the delete form - Jewelry object is 
# is known.  On completion go to /jewels page
class JewelDelete(DeleteView):
  model = Jewelry
  success_url = '/jewels'