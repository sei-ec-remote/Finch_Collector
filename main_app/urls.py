from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('jewels/', views.jewels_index, name='jewels_index'),
]