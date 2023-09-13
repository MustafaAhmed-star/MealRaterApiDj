from rest_framework import serializers
from .models import Meal,Rater
from django.contrib.auth.models import User

class MealSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Meal

        fields = ('id', 'title', 'description', 'no_of_ratings', 'avg_rating')
         

class RatingSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Rater
        fields = ('id','stars','user','meal','review')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}
