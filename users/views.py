from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .serializers import UserRegisterSerializer, UserAuthSerializer, UserConfirmSerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from .models import Users
from random import randint


class AuthAPIView(APIView):

    def post(self, request):
        serializer = UserAuthSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(**serializer.validated_data)

        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response(data={'key': token.key})
        return Response(status=status.HTTP_401_UNAUTHORIZED,
                        data={'User credentials are wrong!'})


class RegistrationAPIView(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data.get('username')
        password = serializer.validated_data.get('password')

        user = User.objects.create_user(username=username, password=password, is_active=False)

        code = randint(100000, 999999)

        Users.objects.create(username=username,
                             code=code)

        return Response(data={'user_id': user.id},
                        status=status.HTTP_201_CREATED)



class ConfirmAPIView(APIView):
    def post(self, request):
        serializer = UserConfirmSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        code = serializer.validated_data.get('code')
        username = serializer.validated_data.get('username')

        try:
            user_code = Users.objects.get(username=username).code

        except Users.DoesNotExist:
            return Response(data={'User does not exist!'}, status=status.HTTP_404_NOT_FOUND)

        if user_code == code:
            user = User.objects.get(username=username)
            user.is_active = True
            user.save()

            return Response(data={'Your account has been activated!'}, status=status.HTTP_202_ACCEPTED)

        return Response(data={'Wrong code!'}, status=status.HTTP_400_BAD_REQUEST)