from rest_framework import serializers
from .models import Director, Movie, Review
from rest_framework.exceptions import ValidationError


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


class DirectorValidateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)


class MovieValidateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    description = serializers.CharField(required=False)
    duration = serializers.TimeField()
    director_id = serializers.IntegerField(min_value=1)

    def validate_director_id(self, director_id):
        try:
            Director.objects.get(id=director_id)
        except Director.DoesNotExist:
            raise ValidationError('Director does not exist')
        return director_id

class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField(required=False)
    stars = serializers.IntegerField(min_value=1, max_value=10)
    movie_id = serializers.IntegerField(min_value=1)

    def validate_movie_id(self, movie_id):
        try:
            Movie.objects.get(id=movie_id)
        except Movie.DoesNotExist:
            raise ValidationError('Movie does not exist')
        return movie_id