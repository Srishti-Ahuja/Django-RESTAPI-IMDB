from rest_framework.exceptions import ValidationError

from .models import Movie, Platform, Review
from .serializers import MovieSerializer, PlatformSerializer, ReviewSerializer
from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView,
                                     ListAPIView)
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrReadOnly

# Create your views here.
class MovieList(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieDetail(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class GenreMovieList(ListAPIView):
    serializer_class = MovieSerializer

    def get_queryset(self):
        return Movie.objects.filter(genre=self.kwargs['genre'])

class PlatformList(ListCreateAPIView):
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer

class PlatformDetail(RetrieveUpdateDestroyAPIView):
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer

class ReviewList(ListCreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Review.objects.filter(movie=self.kwargs['pk'])

    def perform_create(self, serializer):
        reviews = Review.objects.filter(movie=self.kwargs['pk']).filter(reviewer=self.request.user)
        if reviews.exists():
            raise ValidationError("You have reviewed this movie already", 401)
        movie = Movie.objects.get(pk=self.kwargs['pk'])

        #Add rating value to movie
        movie.avg_rating = (movie.avg_rating * movie.no_of_ratings) + serializer.validated_data['rating'] / (movie.no_of_ratings + 1)
        movie.no_of_ratings += 1
        movie.save()

        serializer.save(movie=movie, reviewer=self.request.user)

    def perform_update(self, serializer):
        movie = Movie.objects.get(pk=self.kwargs['pk'])
        movie.avg_rating = (movie.avg_rating * movie.no_of_ratings) + serializer.validated_data['rating'] / (
                    movie.no_of_ratings + 1)
        movie.no_of_ratings += 1
        movie.save()

        serializer.save()


class ReviewDetail(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]