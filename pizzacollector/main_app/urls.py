# main_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('pizza/', views.pizza_index, name='pizza_index'),
    path('pizza/<int:pizza_id>', views.pizza_show, name='pizza_show'),
    path('pizza/create/', views.PizzaCreate.as_view(), name='pizza_create'),
    path('pizza/<int:pk>/update/', views.PizzaUpdate.as_view(), name='pizza_update'),
    path('pizza/<int:pk>/delete/', views.PizzaDelete.as_view(), name='pizza_delete'),


]