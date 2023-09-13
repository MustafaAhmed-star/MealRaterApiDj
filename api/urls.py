from django.urls import path
from rest_framework import routers
from django.urls import include
from .views import MealViewSet,RaterViewSet, UserViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('meals',MealViewSet)
router.register('rating',RaterViewSet)
urlpatterns = [
    path('',include(router.urls)),
]
