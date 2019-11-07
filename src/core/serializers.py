from rest_framework import serializers
from .models import CelestialBody

class CelestialBodySerializer(serializers.ModelSerializer):
    class Meta:
        model = CelestialBody
        fields = (
            'name',
            'mass',
            'age',
            'description',
            'image',
        )