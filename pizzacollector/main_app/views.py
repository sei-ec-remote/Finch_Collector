# main_app/views.py
from django.shortcuts import render



def index(request):
    # render index.html
    return render(request, 'index.html')

# here is our about view
def about(request):
    # render about page
    return render(request, 'about.html')