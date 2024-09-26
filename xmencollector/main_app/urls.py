# main_app/urls.py
# Declare the URLs for our app here

# Import views
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("issues/", views.issues_index, name="issues_index"),
    path("issues/<int:issue_id>/", views.issues_show, name="issues_show"),
    path("issues/create", views.IssueCreate.as_view(), name="issue_create"),
    path("issues/<int:pk>/update/", views.IssueUpdate.as_view(), name="issue_update"),
    path("issues/<int:pk>/delete/", views.IssueDelete.as_view())
]
