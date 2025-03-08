from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Director, Movie, Review
from .serializers import DirectorSerializer, MovieSerializer, ReviewSerializer, DirectorDetailSerializer, MovieDetailSerializer, ReviewDetailSerializer
from rest_framework import status

@api_view(http_method_names=['GET'])
def director_list_api_view(request):
    directors = Director.objects.all()

    serializer = DirectorSerializer(instance=directors, many=True)

    return Response(data=serializer.data)


@api_view(['GET'])
def director_detail_api_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response({'error':'Director not found!'},
                        status=status.HTTP_404_NOT_FOUND)
    data = DirectorDetailSerializer(director).data
    return Response(data=data)

@api_view(http_method_names=['GET'])
def movie_list_api_view(request):
    movies = Movie.objects.all()

    serializer = MovieSerializer(instance=movies, many=True)

    return Response(data=serializer.data)

@api_view(['GET'])
def movie_detail_api_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response({'error': 'Movie not found!'},
                        status=status.HTTP_404_NOT_FOUND)
    data = MovieDetailSerializer(movie).data
    return Response(data=data)


@api_view(http_method_names=['GET'])
def review_list_api_view(request):
    reviews = Review.objects.all()

    serializer = ReviewSerializer(instance=reviews, many=True)

    return Response(data=serializer.data)

@api_view(['GET'])
def review_detail_api_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'error': 'Review not found!'},
                        status=status.HTTP_404_NOT_FOUND)
    data = ReviewDetailSerializer(review).data
    return Response(data=data)