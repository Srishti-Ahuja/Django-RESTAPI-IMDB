from django.urls import path
from .views import (MovieDetail, MovieList, GenreMovieList,
                    PlatformList, PlatformDetail, ReviewList, ReviewDetail)

urlpatterns = [
    path("movies/<int:pk>/reviews/", ReviewList.as_view()),
    path("movies/review/<int:pk>", ReviewDetail.as_view()),
    path("movies/<int:pk>/", MovieDetail.as_view()),
    path("movies/<str:genre>/", GenreMovieList.as_view()),
    path("movies/", MovieList.as_view()),
    path("platforms/", PlatformList.as_view()),
    path("platforms/<int:pk>/", PlatformDetail.as_view()),
]