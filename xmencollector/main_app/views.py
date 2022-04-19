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

def issues_index(request):
    return render(request, "issues/index.html", { "issues": issues })

# Creating a class that will later serve as the model for entries.
class Issue:
    def __init__(self, number, year, cover, writer, artist):
        self.number = number
        self.year = year
        self.cover = cover
        self.writer = writer
        self.artist = artist

# Data to test functionality before database is created and connected.
issues = [
    Issue(135, 1980, "135.jpg", "Chris Claremont", "John Byrne"),
    Issue(141, 1981, "141.jpg", "Chris Claremont", "John Byrne"),
    Issue(173, 1983, "173.jpg", "Chris Claremont", "Paul Smith"),
    Issue(175, 1983, "175.jpg", "Chris Claremont", "Paul Smith")
]
