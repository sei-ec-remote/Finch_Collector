from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('lists/', views.lists_index, name='lists_index'),
    path('lists/<int:list_id>/', views.lists_show, name='lists_show'),
    path('lists/create/', views.ListCreate.as_view(), name='lists_create'),
    path('lists/<int:pk>/update/', views.ListUpdate.as_view(), name='lists_update'),
    path('lists/<int:pk>/delete/', views.ListDelete.as_view(), name='lists_delete')
]