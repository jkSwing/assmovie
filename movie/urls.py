from django.urls import path
from movie.views import get_movies

movie_urls = [
    path('', get_movies),
]
