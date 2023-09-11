from rest_framework import viewsets,status
from .models import Meal,Rater
from .serializers import MealSerialzer,RatingSerialzer
from rest_framework.decorators import action
from rest_framework.response import Response

from django.contrib.auth.models import User
class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerialzer
    @action(detail=True, methods=['post'])
    def rate_meal(self, request, pk=None):
        if 'stars' in request.data:
            '''
            create or update 
            '''
            meal = Meal.objects.get(id=pk)
            stars = request.data['stars']
            username = request.data['username']
            user = User.objects.get(username=username)

            try:
                # update
                rating = Rater.objects.get(user=user.id, meal=meal.id) # specific rate 
                rating.stars = stars
                rating.save()
                serializer = RatingSerialzer(rating, many=False)
                json = {
                    'message': 'Meal Rate Updated',
                    'result': serializer.data
                }
                return Response(json , status=status.HTTP_200_OK)

            except:
                # create if the rate not exist 
                rating = Rater.objects.create(stars=stars, meal=meal, user=user)
                serializer = RatingSerialzer(rating, many=False)
                json = {
                    'message': 'Meal Rate Created',
                    'result': serializer.data
                }
                return Response(json , status=status.HTTP_200_OK)

class RaterViewSet(viewsets.ModelViewSet):
    queryset = Rater.objects.all()
    serializer_class = RatingSerialzer