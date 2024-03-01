# core/serializers.py

from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import *

class CustomUserSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = CustomUsers
        fields = [
            'id',
            'username',
            'full_name',            
            'email',
            'user_type',
            'password',
            'phone_number',
            'address',
            'gender',
            'adhaar_id',
            "driving_id",
            'profile_image',
            'updated',
            ]
        extra_kwargs = {
            'password': {'write_only': True},
        }
        # fields = '__all__'

    def create(self, validated_data):
        user = CustomUsers.objects.create_user(**validated_data)
        return user
class PDLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PDLocation
        fields = '__all__'
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise serializers.ValidationError("Incorrect username or password. Please try again.")

        data['user'] = user
        return data


class ForgotPasswordSerializer(serializers.Serializer):
    # phone_number = serializers.CharField(max_length=15)
    email = serializers.EmailField()

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        # model = Location
        fields = '__all__'
        # fields = ['id', 'name', 'latitude', 'longitude']
class Dummyserial(serializers.Serializer):
   username = serializers.CharField(max_length=50)

class PasswordUpdateSerializer(serializers.Serializer):
    otp = serializers.CharField(max_length=6, min_length=6)
    new_password = serializers.CharField(write_only=True)



