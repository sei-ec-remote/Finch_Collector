from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Jewelry

def index(request):
    return HttpResponse('<h1>Hello World! /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
    return render(request, 'about.html')
 
def index(request):
  return render(request, 'index.html')

def jewels_index(request):
    jewels = Jewelry.objects.all()
    return render(request, 'jewels/index.html', {'jewels': jewels})

def jewels_show(request, jewel_id):
        jewel = Jewelry.objects.get(id=jewel_id)
        return render(request, 'jewels/show.html', {'jewel': jewel})

# use all the fields of our Jewelry model.  Redirect upon successful creation
class JewelCreate(CreateView):
  model = Jewelry
  fields = '__all__'
  success_url = '/jewels'

# No id field.
class JewelUpdate(UpdateView):
  model = Jewelry
  fields = ['type', 'metal', 'description', 'color', 'year']

  # python and postgresql 
  # Now we use a function to determin if a form is valid
  def form_valid(self, form):
    self.object = form.save(commit=False)
    self.object.save()
    # pk is the primary key aka id of the object
    return HttpResponseRedirect('/jewels/' + str(self.object.pk))

class JewelDelete(DeleteView):
  model = Jewelry
  success_url = '/jewels'