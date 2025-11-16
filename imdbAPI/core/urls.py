from django.urls import path
from .views import MovieDetail, MovieList

urlpatterns = [
    path("<int:pk>", MovieDetail),
    path("", MovieList)
]