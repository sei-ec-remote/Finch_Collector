# main_app/views.py
# Declare the routes and client responses here.

from django.shortcuts import render
# # We're now rendering a template instead of sending an HTTP response, so we no longer need this.
# from django.http import HttpResponse

# Create your views here.

# # We're now rendering a template instead of sending an HTTP response, so we no longer need these.
# def index(request):
#     return HttpResponse("<h1> Hi I'm the front page</h1>")
# def about(request):
#     return HttpResponse("<h1>I'm a giant comic book nerd how you doing</h1>")

def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

