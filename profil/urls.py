from django.urls import path
from . import views #kalau titik itu artinya views terletak di dalam 1 folder yang sama.

urlpatterns = [
    path('home/', views.home, name="home"),
    path('cerita/', views.cerita, name="cerita"),
    path('berita/', views.berita, name="berita"),
]
