from rest_framework import serializers
from .models import Movie, Platform, Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
        extra_kwargs = {
            'movie': {'read_only': True},
            'reviewer': {'read_only': True}
        }

class MovieSerializer(serializers.ModelSerializer):
    reviews = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = '__all__'
        extra_kwargs = {
            'avg_rating': {'read_only': True},
            'no_of_ratings': {'read_only': True}
        }

class PlatformSerializer(serializers.ModelSerializer):
    movies = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Platform
        fields = '__all__'