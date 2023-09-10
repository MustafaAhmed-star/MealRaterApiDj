from rest_framework import serializers
from .models import Meal,Rater

class MealSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ('id','title','description')
class RatingSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Rater
        fields = ('id','stars','user','meal','review')