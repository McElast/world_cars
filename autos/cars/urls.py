from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CarViewSet

cars_router = DefaultRouter()
cars_router.register('cars', CarViewSet, basename='cars')

urlpatterns = [
    path('', include(cars_router.urls))
]
