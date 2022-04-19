# main_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('pizza/', views.pizza_index, name='pizza_index'),
    path('pizza/<int:pizza_id>', views.pizza_show, name='pizza_show'),

]