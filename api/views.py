from rest_framework import viewsets
from .models import Meal,Rater
from .serializers import MealSerialzer,RatingSerialzer

class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerialzer


class RaterViewSet(viewsets.ModelViewSet):
    queryset = Rater.objects.all()
    serializer_class = RatingSerialzer