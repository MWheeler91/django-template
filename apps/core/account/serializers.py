# from rest_framework import serializers
# from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import ValidationError
from error_logging.logger import ErrorLogger
from .models import *
from utils.common import catch_errors

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password']

    def validate(self, attrs):
        try:
            email_exists = User.objects.filter(email=attrs["email"]).exists()
            if email_exists:
                raise ValidationError("Email has already been used")
            return super().validate(attrs)
        except Exception as e:
            ErrorLogger.log(e, app="catalog", user=None)

    def create(self, validated_data):
        try:
            print(validated_data)
            password = validated_data.pop("password")
            user = super().create(validated_data)
            user.set_password(password)
            user.save()
            Token.objects.create(user=user)
            return user
        except Exception as e:
                ErrorLogger.log(e, app="catalog", user=None)




