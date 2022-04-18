# main_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('drinks/', views.drinks_index, name='drinks_index'),
    path('drinks/<int:drink_id>/', views.drinks_show, name='drinks_show'),
    path('drinks/create/', views.DrinkCreate.as_view(), name='drinks_create'),
    path('drinks/<int:pk>/update/', views.DrinkUpdate.as_view(), name='drinks_update'),
    path('drinks/<int:pk>/delete/', views.DrinkDelete.as_view(), name='drinks_delete')
]