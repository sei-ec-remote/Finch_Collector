# main_app/urls.py
# Declare the URLs for our app here

# Import views
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
]
