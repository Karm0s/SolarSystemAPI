from django.shortcuts import render

from rest_framework.generics import ListAPIView
from .serializers import CelestialBodySerializer

from .models import CelestialBody

class ListCeletialBodies(ListAPIView):
    serializer_class = CelestialBodySerializer
    queryset = CelestialBody.objects.all()


