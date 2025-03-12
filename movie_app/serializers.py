from rest_framework import serializers
from .models import Director, Movie, Review


class DirectorSerializer(serializers.ModelSerializer):

    movies_count = serializers.SerializerMethodField()

    class Meta:
        model = Director
        fields = 'name movies_count'.split()
        depth = 1

    def get_movies_count(self, object):
        return object.director.count()

class DirectorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = 'id title'.split()

class MovieDetailSerializer(serializers.ModelSerializer):
    director = DirectorSerializer().field_name

    class Meta:
        model = Movie
        fields = '__all__'

class AllReviewSerializer(serializers.ModelSerializer):
    movie = MovieSerializer()

    class Meta:
        model = Review
        fields = 'id stars movie'.split()

class ReviewDetailSerializer(serializers.ModelSerializer):
    movie = MovieSerializer()

    class Meta:
        model = Review
        fields = '__all__'


class MovieReviewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = 'id title rating reviews'.split()
        depth = 1


