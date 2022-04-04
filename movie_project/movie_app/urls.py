from . import views as movie
from django.urls import path

urlpatterns = [
    path('', movie.show_all_movie),
    path('movie/<slug:slug_movie>', movie.show_one_movie, name='movie-detail'),
]