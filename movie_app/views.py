from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Director, Movie, Review
from .serializers import DirectorSerializer, MovieSerializer, AllReviewSerializer, DirectorDetailSerializer, \
    MovieDetailSerializer, ReviewDetailSerializer, MovieReviewsSerializer
from rest_framework import status

@api_view(http_method_names=['GET', 'POST'])
def director_list_create_api_view(request):
    if request.method == 'GET':

        directors = Director.objects.all()
        serializer = DirectorSerializer(instance=directors, many=True)

        return Response(data=serializer.data)

    elif request.method == 'POST':
        name = request.data.get('name')

        director = Director.objects.create(name=name)


        return Response(data=DirectorDetailSerializer(director).data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def director_detail_api_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response({'error':'Director not found!'},
                        status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        data = DirectorDetailSerializer(director).data
        return Response(data=data)

    elif request.method == 'DELETE':
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        director.name = request.data.get('name')
        director.save()
        return Response(data=DirectorDetailSerializer(director).data, status=status.HTTP_201_CREATED)

@api_view(http_method_names=['GET', 'POST'])
def movie_list_create_api_view(request):
    if request.method == 'GET':
        movies = Movie.objects.all()

        serializer = MovieSerializer(instance=movies, many=True)

        return Response(data=serializer.data)

    elif request.method == 'POST':
        title = request.data.get('title')
        description = request.data.get('description')
        duration = request.data.get('duration')
        director_id = request.data.get('director_id')

        movie = Movie.objects.create(title=title,
                                     description=description,
                                     duration=duration,
                                     director_id=director_id)


        return Response(data=MovieDetailSerializer(movie).data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail_api_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response({'error': 'Movie not found!'},
                        status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        data = MovieDetailSerializer(movie).data
        return Response(data=data)

    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        movie.title = request.data.get('title')
        movie.description = request.data.get('description')
        movie.duration = request.data.get('duration')
        movie.director_id = request.data.get('director_id')
        movie.save()
        return Response(data=MovieDetailSerializer(movie).data, status=status.HTTP_201_CREATED)


@api_view(http_method_names=['GET', 'POST'])
def review_list_create_api_view(request):
    if request.method == 'GET':
        reviews = Review.objects.all()

        serializer = AllReviewSerializer(instance=reviews, many=True)

        return Response(data=serializer.data)

    elif request.method == 'POST':
        text = request.data.get('text')
        movie_id = request.data.get('movie_id')
        stars = request.data.get('stars')

        review = Review.objects.create(text=text, movie_id=movie_id, stars=stars)


        return Response(data=ReviewDetailSerializer(review).data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def review_detail_api_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'error': 'Review not found!'},
                        status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        data = ReviewDetailSerializer(review).data
        return Response(data=data)

    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        review.text = request.data.get('text')
        review.movie_id = request.data.get('movie_id')
        review.stars = request.data.get('stars')
        review.save()
        return Response(data=ReviewDetailSerializer(review).data, status=status.HTTP_201_CREATED)


@api_view(http_method_names=['GET'])
def review_movie_list_api_view(request):
    reviews = Movie.objects.all()

    serializer = MovieReviewsSerializer(instance=reviews, many=True)

    return Response(data=serializer.data)