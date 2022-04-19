# main_app/views.py
# Declare the routes and client responses here.

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1> Hi I'm the front page</h1>")

