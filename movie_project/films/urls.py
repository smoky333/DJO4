from django.urls import path
from . import views

urlpatterns = [
    path('', views.film_list, name='film_list'),
    path('add/', views.add_film, name='add_film'),
    path('delete/<int:pk>/', views.delete_film, name='delete_film'),
]
