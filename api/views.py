from rest_framework import viewsets,status
from .models import Meal,Rater
from .serializers import MealSerialzer,RatingSerialzer, UserSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication

from rest_framework.permissions import  AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.authtoken.models import Token

from django.contrib.auth.models import User
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # #authentication_classes = (TokenAuthentication, )
    permission_classes = (AllowAny,)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        token, created = Token.objects.get_or_create(user=serializer.instance)
        return Response({
                'token': token.key, 
                }, 
            status=status.HTTP_201_CREATED)
    
    def list(self, request, *args, **kwargs):
        response = {'message': 'You cant create rating like that'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerialzer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated,)
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
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated)
    def update(self, request, *args, **kwargs):
        response = {
            'message': 'Invalid way to create or update '
            }

        return Response(response, status=status.HTTP_400_BAD_REQUEST)
    
    def create(self, request, *args, **kwargs):
        response = {
            'message': 'Invalid way to create or update '
            }

        return Response(response, status=status.HTTP_400_BAD_REQUEST)