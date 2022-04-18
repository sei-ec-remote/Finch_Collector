# main_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('albums/', views.albums_index, name='albums_index'),
    path('albums/<int:album_id>/' , views.albums_show, name = 'albums_show'),
    path('albums/create/', views.AlbumCreate.as_view(), name='albums_create'),
    path('albums/<int:pk>/update/', views.AlbumUpdate.as_view(), name='albums_update'),
    path('cats/<int:pk>/delete/', views.AlbumDelete.as_view(), name='albums_delete')
]