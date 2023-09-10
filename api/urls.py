from django.urls import path
from rest_framework import routers
from django.urls import include
from .views import MealViewSet,RaterViewSet

router = routers.DefaultRouter()
router.register('meals',MealViewSet)
router.register('rating',RaterViewSet)
urlpatterns = [
    path('',include(router.urls)),
]
