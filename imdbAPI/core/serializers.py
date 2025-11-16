from rest_framework import serializers
from .models import Movie, Platform, Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    reviews = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = '__all__'

class PlatformSerializer(serializers.ModelSerializer):
    movies = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Platform
        fields = '__all__'