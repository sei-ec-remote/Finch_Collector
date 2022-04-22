from django.urls import path 
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('recipes/', views.recipes_index, name='recipe_index'),
    path('recipes/<int:recipe_id>/', views.recipes_show, name='recipes_show'),
    path('recipes/create/', views.RecipeCreate.as_view(), name='recipes_create')

]