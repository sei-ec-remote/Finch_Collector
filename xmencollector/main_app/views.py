# main_app/views.py
# Declare the routes and client responses here.

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1> Hi I'm the front page</h1>")

def about(request):
    return HttpResponse("<h1>I'm a giant comic book nerd how you doing</h1>")

