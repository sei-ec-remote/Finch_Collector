from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('dogs/', views.dogs_index, name='dogs_index'),
    path('dogs/<int:dog_id>/', views.dogs_show, name='dogs_show')
]