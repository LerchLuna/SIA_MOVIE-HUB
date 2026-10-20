from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from . import views

urlpatterns = [
    path( 'admin/', admin.site.urls),
    path('', views.landing, name='landing'),
    path( 'movie_list/', views.movie_list, name='movie_list'),
    path('add/', views.add_movie, name='add_movie'),
    path('edit/<int:pk>/', views.edit_movie, name='edit_movie'),
    path('delete/<int:pk>/', views.delete_movie, name='delete_movie'),
]