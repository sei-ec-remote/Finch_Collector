from django.urls import path
from . import views

# These are all the routes for the Jewelry Site and the names of the 
# functions which django will call in views.py
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('jewels/', views.jewels_index, name='jewels_index'),
    path('jewels/<int:jewel_id>/', views.jewels_show, name='jewels_show'),
    path('jewels/create/', views.JewelCreate.as_view(), name='jewels_create'),
    path('jewels/<int:pk>/update/', views.JewelUpdate.as_view(), name='jewels_update'),
    path('jewels/<int:pk>/delete/', views.JewelDelete.as_view(), name='jewels_delete'), 
]