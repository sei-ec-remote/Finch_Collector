from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from .models import List


# Create your views here.
def index(request):
  return render(request, 'index.html')

def about(request):
 return render(request, 'about.html')

# class List:
#     def __init__(self, title, description, status, day):
#         self.title = title
#         self.description = description
#         self.status = status
#         self.day = day

# lists = [
#     List('Laundry', '5 load of laundry to do', 'In Progress', 'Tuesday'),
#     List('Dishes', 'unload and load dishes', 'In Progress', 'Wednesday'),
#     List('Deliverable', 'Django deliverable', 'In Progress', 'Monday')
# ]

def lists_index(request):
    lists = List.objects.all()
    return render(request, 'lists/index.html', {'lists': lists})

def lists_show(request, list_id):
    list = List.objects.get(id=list_id)
    return render(request, 'lists/show.html', {'list': list})

class ListCreate(CreateView):
    model = List
    fields = '__all__'
    success_url = '/lists'

class ListUpdate(UpdateView):
    model = List
    fields = ['title', 'description', 'status', 'day']
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return HttpResponseRedirect('/lists/' + str(self.object.pk))

class ListDelete(DeleteView):
    model = List
    success_url = '/lists'