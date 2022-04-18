from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.

def index(request):
    # return HttpResponse('<h1> Woof! υ´• ﻌ •`υ </h1>')
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

