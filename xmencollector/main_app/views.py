# main_app/views.py
# Declare the routes and client responses here.

from django.shortcuts import render
from .models import Issue
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponsePermanentRedirect, HttpResponseRedirect

# # We're now rendering a template instead of sending an HTTP response, so we no longer need this.
# from django.http import HttpResponse

class IssueCreate(CreateView):
    model = Issue
    fields = "__all__"
    success_url = "/issues"

class IssueUpdate(UpdateView):
    model = Issue
    fields = ["number", "year", "cover", "writer", "artist"]
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return HttpResponseRedirect("/issues/" + str(self.object.pk))

class IssueDelete(DeleteView):
    model = Issue
    success_url = "/issues"


# # We're now rendering a template instead of sending an HTTP response, so we no longer need these.
# def index(request):
#     return HttpResponse("<h1> Hi I'm the front page</h1>")
# def about(request):
#     return HttpResponse("<h1>I'm a giant comic book nerd how you doing</h1>")

def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

# # Our info will now come from the database so this route must be rewritten.
# def issues_index(request):
#     return render(request, "issues/index.html", { "issues": issues })

# INDEX view for all comic issues
def issues_index(request):
    issues = Issue.objects.all()
    return render(request, "issues/index.html", { "issues": issues })

# SHOW view for individual issues
def issues_show(request, issue_id):
    issue = Issue.objects.get(id=issue_id)
    return render(request, "issues/show.html", { "issue": issue })


# # # Creating a class that will later serve as the model for entries.
# # Now removing that class as we've shifted to the database.
# class Issue:
#     def __init__(self, number, year, cover, writer, artist):
#         self.number = number
#         self.year = year
#         self.cover = cover
#         self.writer = writer
#         self.artist = artist
#
# # # Data to test functionality before database is created and connected.
# # Removing the test data now that the database is up and running.
# issues = [
#     Issue(135, 1980, "135.jpg", "Chris Claremont", "John Byrne"),
#     Issue(141, 1981, "141.jpg", "Chris Claremont", "John Byrne"),
#     Issue(173, 1983, "173.jpg", "Chris Claremont", "Paul Smith"),
#     Issue(175, 1983, "175.jpg", "Chris Claremont", "Paul Smith")
# ]
