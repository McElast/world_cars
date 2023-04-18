from rest_framework import serializers

from .models import Car, CarImage


class CarImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = CarImage
        fields = ['photo']


class CarSerializer(serializers.ModelSerializer):
    images = CarImageSerializer(read_only=True, many=True)

    class Meta:
        model = Car
        fields = ['name', 'year', 'images']
