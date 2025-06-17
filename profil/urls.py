from django.conf import settings
from django.urls import path
from . import views #kalau titik itu artinya views terletak di dalam 1 folder yang sama.
from django.conf.urls.static import static



urlpatterns = [
    path('home/', views.home, name="home"),
    path('cerita/', views.cerita, name="cerita"),
    path('berita/', views.berita, name="berita"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)