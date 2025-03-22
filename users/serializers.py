from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError


class UserBaseSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField()


class UserAuthSerializer(UserBaseSerializer):
    pass


class UserRegisterSerializer(UserBaseSerializer):
    def validate_username(self, username):
        try:
            User.objects.get(username=username)
        except:
            return username
        raise ValidationError('User already exists!')


class UserConfirmSerializer(UserBaseSerializer):
    code = serializers.IntegerField()

    def validate_code(self, code):
        try:
            User.objects.get(code=code)
        except:
            return code
        raise ValidationError('Wrong code!')